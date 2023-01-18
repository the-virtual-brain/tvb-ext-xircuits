# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import json
import os
import sys
from datetime import datetime
from urllib.error import HTTPError
import pyunicore.client as unicore_client
from pyunicore.helpers.jobs import Status as unicore_status
from pyunicore.credentials import AuthenticationFailedException
from tvbwidgets.core.auth import get_current_token

import tvbextxircuits._version as xircuits_version
from tvbextxircuits.hpc_config.parse_files import get_files_to_upload
from tvbextxircuits.utils import STORAGE_CONFIG_FILE, STORE_RESULTS_DIR, FOLDER_PATH_KEY, BUCKET_NAME_KEY


class PyunicoreSubmitter(object):
    storage_name = 'HOME'
    env_dir = 'tvb_xircuits'
    env_name = 'venv'
    modules = {'DAINT-CSCS': 'cray-python', 'JUSUF': 'Python'}
    pip_libraries = 'tvb-ext-xircuits tvb-data'
    EXECUTABLE_KEY = 'Executable'
    PROJECT_KEY = 'Project'
    JOB_TYPE_KEY = 'Job type'
    INTERACTIVE_KEY = 'interactive'

    def __init__(self, site, project):
        self.site = site
        self.project = project

    @property
    def _activate_command(self):
        return f'source ${self.storage_name}/{self.env_dir}/{self.env_name}/bin/activate'

    @property
    def _module_load_command(self):
        return f'module load {self.modules.get(self.site, "")}'

    @property
    def _create_env_command(self):
        return f'cd ${self.storage_name}/{self.env_dir} && rm -rf {self.env_name} && python -mvenv {self.env_name}'

    @property
    def _install_dependencies_command(self):
        return f'pip install -U pip && pip install allensdk && pip install {self.pip_libraries}'

    def connect_client(self):
        print(f"Connecting to {self.site}...")
        token = get_current_token()
        transport = unicore_client.Transport(token)
        registry = unicore_client.Registry(transport, unicore_client._HBP_REGISTRY_URL)
        sites = registry.site_urls

        try:
            site_url = sites[self.site]
        except KeyError:
            print(f'Site {self.site} seems to be down for the moment.')
            return None

        try:
            client = unicore_client.Client(transport, site_url)
        except (AuthenticationFailedException, HTTPError):
            print(f'Authentication to {self.site} failed, you might not have permissions to access it.', flush=True)
            return None

        print(f'Authenticated to {self.site} with success.', flush=True)
        return client

    def _check_environment_ready(self, home_storage):
        # Pyunicore listdir method returns directory names suffixed by '/'
        if f"{self.env_dir}/" not in home_storage.listdir():
            home_storage.mkdir(self.env_dir)
            print(f"Environment directory not found in HOME, will be created.")
            return False

        if f"{self.env_dir}/{self.env_name}/" not in home_storage.listdir(self.env_dir):
            print(f"Environment not found in HOME, will be created.")
            return False

        try:
            # Check whether tvb-ext-xircuits is installed in HPC env and if version is updated
            site_packages = home_storage.listdir(f'{self.env_dir}/{self.env_name}/lib/python3.9/site-packages')
            files = [file for file in site_packages if "tvb_ext_xircuits" in file]
            assert len(files) >= 1
            remote_version = files[0].split("tvb_ext_xircuits-")[1].split('.dist-info')[0]
            local_version = xircuits_version.__version__
            if remote_version != local_version:
                print(f"Found an older version {remote_version} of tvb-ext-xircuits installed in the environment, "
                      f"will recreate it with {local_version}.")
                return False
            return True
        except HTTPError as e:
            print(f"Could not find site-packages in the environment, will recreate it: {e}")
            return False
        except AssertionError:
            print(f"Could not find tvb-ext-xircuits installed in the environment, will recreate it.")
            return False
        except IndexError:
            print(f"Could not find tvb-ext-xircuits installed in the environment, will recreate it.")
            return False

    def _search_for_home_dir(self, client):
        print(f"Accessing storages on {self.site}...", flush=True)
        num = 10
        offset = 0
        storages = client.get_storages(num=num, offset=offset)
        while len(storages) > 0:
            for storage in storages:
                if storage.resource_url.endswith(self.storage_name):
                    return storage
            offset += num
            storages = client.get_storages(num=num, offset=offset)
        return None

    def _format_date_for_job(self, job):
        date = datetime.strptime(job.properties['submissionTime'], '%Y-%m-%dT%H:%M:%S+%f')
        return date.strftime('%m.%d.%Y, %H:%M:%S')

    def _dev_mode(self, home_storage, client):
        """
        The purpose of this method is to allow developers to test packages on HPC before releasing them on Pypi.
        First step is to run the build command under the tvb-ext-xircuits folder: python -m build
        It will generate the 'dist' folder with a WHL and TAR.GZ packages for tvb-ext-xircuits.
        Then, make sure to call this method from submit_job method before launching the workflow job.
        """
        local_package_name = f'tvb_ext_xircuits-{xircuits_version.__version__}-py3-none-any.whl'
        print(f"You are running in dev mode, starting to install {local_package_name} on HPC {self.site}...")
        home_storage.rm(local_package_name)
        home_storage.upload(
            input_file=f'dist/{local_package_name}',
            destination=f'{self.env_dir}/{local_package_name}')
        self.pip_libraries = self.pip_libraries.replace('tvb-ext-xircuits', local_package_name)
        job_description = {
            self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._create_env_command} && "
                                 f"{self._activate_command} && {self._install_dependencies_command}",
            self.PROJECT_KEY: self.project,
            self.JOB_TYPE_KEY: self.INTERACTIVE_KEY}
        job_env_prep = client.new_job(job_description, inputs=[])
        print(f"Job is running at {self.site}: {job_env_prep.working_dir.properties['mountPoint']}. "
              f"Submission time is: {self._format_date_for_job(job_env_prep)}. "
              f"Waiting for job to finish..."
              f"It can also be monitored interactively with the Monitor HPC button.", flush=True)
        job_env_prep.poll()
        if job_env_prep.properties['status'] == unicore_status.FAILED:
            print(f"Encountered an error during environment setup, stopping execution.")
            return
        print(f"Successfully finished the environment setup.")

    def submit_job(self, executable, inputs, do_stage_out):
        client = self.connect_client()
        if client is None:
            print(f"Could not connect to {self.site}, stopping execution.")
            return

        home_storage = self._search_for_home_dir(client)
        if home_storage is None:
            print(f"Could not find a {self.storage_name} storage on {self.site}, stopping execution.")
            return

        is_env_ready = self._check_environment_ready(home_storage)

        if is_env_ready:
            print(f"Environment is already prepared, it won't be recreated.")
            # self._dev_mode(home_storage, client)
        else:
            print(f"Preparing environment in your {self.storage_name} folder...", flush=True)
            job_description = {
                self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._create_env_command} && "
                                     f"{self._activate_command} && {self._install_dependencies_command}",
                self.PROJECT_KEY: self.project,
                self.JOB_TYPE_KEY: self.INTERACTIVE_KEY}
            job_env_prep = client.new_job(job_description, inputs=[])
            print(f"Job is running at {self.site}: {job_env_prep.working_dir.properties['mountPoint']}. "
                  f"Submission time is: {self._format_date_for_job(job_env_prep)}. "
                  f"Waiting for job to finish..."
                  f"It can also be monitored interactively with the Monitor HPC button.", )
            job_env_prep.poll()
            if job_env_prep.properties['status'] == unicore_status.FAILED:
                print(f"Encountered an error during environment setup, stopping execution.")
                return
            print(f"Successfully finished the environment setup.")

        print("Launching workflow...", flush=True)
        job_description = {
            self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._activate_command} && "
                                 f"python {executable} --is_hpc_launch=True",
            self.PROJECT_KEY: self.project}
        job_workflow = client.new_job(job_description, inputs=inputs)
        print(f"Job is running at {self.site}: {job_workflow.working_dir.properties['mountPoint']}. "
              f"Submission time is: {self._format_date_for_job(job_workflow)}.", flush=True)
        print('Finished remote launch.', flush=True)

        if do_stage_out:
            self.monitor_job(job_workflow)

        else:
            print('You can use Monitor HPC button to monitor it.', flush=True)

    def monitor_job(self, job):
        print('Waiting for job to finish...'
              'It can also be monitored interactively with the Monitor HPC button.', flush=True)
        job.poll()

        if job.properties['status'] == unicore_status.FAILED:
            print(f"Job finished with errors.", flush=True)
            return
        print(f"Job finished with success. Staging out the results...", flush=True)
        self.stage_out_results(job)
        print(f"Finished execution.", flush=True)

    def stage_out_results(self, job):
        storage_config = {}
        content = job.working_dir.listdir()

        results_dirname = None
        for file_name in content.keys():
            if file_name.startswith(STORE_RESULTS_DIR):
                results_dirname = file_name

        if results_dirname is None:
            print(f"Could not find results folder for this job. Nothing to stage out.", flush=True)
            return

        print(f"Found sub dir: {results_dirname}", flush=True)
        results_content = job.working_dir.listdir(results_dirname)

        storage_config_file = content.get(STORAGE_CONFIG_FILE)
        if storage_config_file is None:
            print(f"Could not find file: {STORAGE_CONFIG_FILE}, downloading results to default location...", flush=True)
        else:
            storage_config_file.download(STORAGE_CONFIG_FILE)
            with open(STORAGE_CONFIG_FILE) as f:
                storage_config = json.load(f)
            os.remove(STORAGE_CONFIG_FILE)

        if storage_config.get(FOLDER_PATH_KEY) is not None:
            results_dirname = os.path.join(storage_config.get('folder_path'), results_dirname)

        if storage_config.get(BUCKET_NAME_KEY) is None:
            self._stage_out_results_to_drive(results_content, results_dirname)
        else:
            self._stage_out_results_to_bucket(results_content, results_dirname)

    def _stage_out_results_to_drive(self, results_folder_content, results_dirname):
        if os.path.isdir(results_dirname):
            results_dirname += f"_{datetime.now().strftime('%m.%d.%Y_%H:%M:%S')}"
        os.mkdir(results_dirname)

        print(f"Downloading results to {results_dirname}...", flush=True)
        for key, val in results_folder_content.items():
            if isinstance(val, unicore_client.PathFile):
                val.download(os.path.join(results_dirname, os.path.basename(key)))

    def _stage_out_results_to_bucket(self, results_folder_content, results_dirname):
        # TODO: stage-out to bucket as well
        print("TODO: Downloading result to Bucket...")


def get_xircuits_file():
    """
    :return: the file name and the absolute path for the compiled workflow file
    """
    # check that compiled .xircuits file is correctly passed as argument
    file_arg = sys.argv[1]
    print(f'Identified the executable file: {file_arg}', flush=True)

    if os.path.exists(file_arg):
        full_path = os.path.abspath(file_arg)
    else:
        print(f"Cannot find the executable file: {file_arg}", flush=True)
        full_path = None

    filename = os.path.basename(file_arg)

    return filename, full_path


def launch_job(site, project, workflow_file_name, workflow_file_path, files_to_upload, do_stage_out=False):
    """
    Submit a job to a EBRAINS HPC site
    :param site: unicore site
    :param workflow_file_name: base name of compiled workflow file
    :param workflow_file_path: absolute path of compiled workflow file
    :param files_to_upload: list of additional files that need to be sent to the HPC server
    :return: None
    """
    inputs = [workflow_file_path]
    if files_to_upload:
        inputs.extend(files_to_upload)

    PyunicoreSubmitter(site, project).submit_job(workflow_file_name, inputs, do_stage_out)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(f"Please provide the HPC project to run this job within, stopping execution.")
    else:
        workflow_name, workflow_path = get_xircuits_file()
        print("Preparing job...", flush=True)
        files_to_upload = get_files_to_upload(xircuits_file_path=workflow_path)
        site_arg = sys.argv[2]
        project_arg = sys.argv[3]
        stage_out_arg = sys.argv[4]
        do_stage_out = True if stage_out_arg == 'true' else False
        launch_job(site=site_arg, project=project_arg, workflow_file_name=workflow_name,
                   workflow_file_path=workflow_path, files_to_upload=files_to_upload, do_stage_out=do_stage_out)

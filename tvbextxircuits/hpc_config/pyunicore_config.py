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
from io import BytesIO
from urllib.error import HTTPError
import pyunicore.client as unicore_client
import requests
from pyunicore.helpers.jobs import Status as unicore_status
from pyunicore.credentials import AuthenticationFailedException
from tvb_ext_bucket.ebrains_drive_wrapper import BucketWrapper
from tvb_ext_bucket.exceptions import CollabAccessError
from tvbwidgets.core.auth import get_current_token

import tvbextxircuits._version as xircuits_version
from tvbextxircuits.hpc_config.parse_files import get_files_to_upload
from tvbextxircuits.logger.builder import get_logger
from tvbextxircuits.utils import *
from xai_components.xai_storage.store_results import StoreResultsToDrive

LOGGER = get_logger('tvbextxircuits.hpc_config.pyunicore_config')


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
        LOGGER.info(f"Connecting to {self.site}...")
        token = get_current_token()
        transport = unicore_client.Transport(token)
        registry = unicore_client.Registry(transport, unicore_client._HBP_REGISTRY_URL)
        sites = registry.site_urls

        try:
            site_url = sites[self.site]
        except KeyError:
            LOGGER.error(f'Site {self.site} seems to be down for the moment.')
            return None

        try:
            client = unicore_client.Client(transport, site_url)
        except (AuthenticationFailedException, HTTPError):
            LOGGER.error(f'Authentication to {self.site} failed, you might not have permissions to access it.')
            return None

        LOGGER.info(f'Authenticated to {self.site} with success.')
        return client

    def _check_environment_ready(self, home_storage):
        # Pyunicore listdir method returns directory names suffixed by '/'
        if f"{self.env_dir}/" not in home_storage.listdir():
            home_storage.mkdir(self.env_dir)
            LOGGER.info(f"Environment directory not found in HOME, will be created.")
            return False

        if f"{self.env_dir}/{self.env_name}/" not in home_storage.listdir(self.env_dir):
            LOGGER.info(f"Environment not found in HOME, will be created.")
            return False

        try:
            # Check whether tvb-ext-xircuits is installed in HPC env and if version is updated
            site_packages = home_storage.listdir(f'{self.env_dir}/{self.env_name}/lib/python3.9/site-packages')
            files = [file for file in site_packages if "tvb_ext_xircuits" in file]
            assert len(files) >= 1
            remote_version = files[0].split("tvb_ext_xircuits-")[1].split('.dist-info')[0]
            local_version = xircuits_version.__version__
            if remote_version != local_version:
                LOGGER.info(f"Found an older version {remote_version} of tvb-ext-xircuits installed in the "
                            f"environment, will recreate it with {local_version}.")
                return False
            return True
        except HTTPError as e:
            LOGGER.info(f"Could not find site-packages in the environment, will recreate it: {e}")
            return False
        except AssertionError:
            LOGGER.info(f"Could not find tvb-ext-xircuits installed in the environment, will recreate it.")
            return False
        except IndexError:
            LOGGER.info(f"Could not find tvb-ext-xircuits installed in the environment, will recreate it.")
            return False

    def _search_for_home_dir(self, client):
        LOGGER.info(f"Accessing storages on {self.site}...")
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
        LOGGER.info(f"You are running in dev mode, starting to install {local_package_name} on HPC {self.site}...")
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
        LOGGER.info(f"Job is running at {self.site}: {job_env_prep.working_dir.properties['mountPoint']}. "
                    f"Submission time is: {self._format_date_for_job(job_env_prep)}. "
                    f"Waiting for job to finish..."
                    f"It can also be monitored interactively with the Monitor HPC button.")
        job_env_prep.poll()
        if job_env_prep.properties['status'] == unicore_status.FAILED:
            LOGGER.error(f"Encountered an error during environment setup, stopping execution.")
            return
        LOGGER.info(f"Successfully finished the environment setup.")

    def submit_job(self, executable, inputs, do_stage_out):
        client = self.connect_client()
        if client is None:
            LOGGER.error(f"Could not connect to {self.site}, stopping execution.")
            return

        home_storage = self._search_for_home_dir(client)
        if home_storage is None:
            LOGGER.error(f"Could not find a {self.storage_name} storage on {self.site}, stopping execution.")
            return

        is_env_ready = self._check_environment_ready(home_storage)

        if is_env_ready:
            LOGGER.info(f"Environment is already prepared, it won't be recreated.")
            # self._dev_mode(home_storage, client)
        else:
            LOGGER.info(f"Preparing environment in your {self.storage_name} folder...")
            job_description = {
                self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._create_env_command} && "
                                     f"{self._activate_command} && {self._install_dependencies_command}",
                self.PROJECT_KEY: self.project,
                self.JOB_TYPE_KEY: self.INTERACTIVE_KEY}
            job_env_prep = client.new_job(job_description, inputs=[])
            LOGGER.info(f"Job is running at {self.site}: {job_env_prep.working_dir.properties['mountPoint']}. "
                        f"Submission time is: {self._format_date_for_job(job_env_prep)}. "
                        f"Waiting for job to finish..."
                        f"It can also be monitored interactively with the Monitor HPC button.")
            job_env_prep.poll()
            if job_env_prep.properties['status'] == unicore_status.FAILED:
                LOGGER.error(f"Encountered an error during environment setup, stopping execution.")
                return
            LOGGER.info(f"Successfully finished the environment setup.")

        LOGGER.info("Launching workflow...")
        job_description = {
            self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._activate_command} && "
                                 f"python {executable} --is_hpc_launch=True",
            self.PROJECT_KEY: self.project}
        job_workflow = client.new_job(job_description, inputs=inputs)
        LOGGER.info(f"Job is running at {self.site}: {job_workflow.working_dir.properties['mountPoint']}. "
                    f"Submission time is: {self._format_date_for_job(job_workflow)}.")
        LOGGER.info('Finished remote launch.')

        if do_stage_out:
            self.monitor_job(job_workflow)

        else:
            LOGGER.info('You can use Monitor HPC button to monitor it.')

    def monitor_job(self, job):
        LOGGER.info('Waiting for job to finish...'
                    'It can also be monitored interactively with the Monitor HPC button.')
        job.poll()

        if job.properties['status'] == unicore_status.FAILED:
            LOGGER.error(f"Job finished with errors.")
            return
        LOGGER.info(f"Job finished with success. Staging out the results...")
        self.stage_out_results(job)
        LOGGER.info(f"Finished execution.")

    def stage_out_results(self, job):
        content = job.working_dir.listdir()

        results_dirname = None
        for file_name in content.keys():
            if file_name.startswith(STORE_RESULTS_DIR):
                results_dirname = file_name

        if results_dirname is None:
            LOGGER.info(f"Could not find results folder for this job. Nothing to stage out.")
            return

        LOGGER.info(f"Found sub dir: {results_dirname}")
        results_content = job.working_dir.listdir(results_dirname)

        storage_config_file = content.get(STORAGE_CONFIG_FILE)
        if storage_config_file is None:
            LOGGER.info(f"Could not find file: {STORAGE_CONFIG_FILE}")
            LOGGER.info("Could not finalize the stage out. "
                        "Please download your results manually using the Monitor HPC button.")
            return
        else:
            storage_config_file.download(STORAGE_CONFIG_FILE)
            with open(STORAGE_CONFIG_FILE) as f:
                storage_config = json.load(f)
            os.remove(STORAGE_CONFIG_FILE)

        collab_name = storage_config.get(COLLAB_NAME_KEY)
        bucket_name = storage_config.get(BUCKET_NAME_KEY)
        folder_path = storage_config.get(FOLDER_PATH_KEY)

        if bucket_name is None:
            self._stage_out_results_to_drive(results_content, collab_name, folder_path, results_dirname)
        else:
            self._stage_out_results_to_bucket(results_content, bucket_name, folder_path, results_dirname)

    def _stage_out_results_to_drive(self, results_folder_content, collab_name, folder_path, results_dirname):
        LOGGER.info(f"Storing results to Collab {collab_name} under {folder_path}/{results_dirname} ...")
        sub_folder = StoreResultsToDrive.create_results_folder_in_collab(collab_name, folder_path, results_dirname)

        for key, val in results_folder_content.items():
            if isinstance(val, unicore_client.PathFile):
                with BytesIO() as in_memory_file:
                    val.download(in_memory_file)
                    file = sub_folder.upload(in_memory_file.getvalue(), os.path.basename(key))
                    LOGGER.info(f'File {file.path} has been stored to Drive')

    def _stage_out_results_to_bucket(self, results_folder_content, bucket_name, folder_path, results_dirname):
        LOGGER.info(f"Storing results to Bucket {bucket_name} under {folder_path}/{results_dirname}")
        bucket_wrapper = BucketWrapper()

        for key, val in results_folder_content.items():
            if isinstance(val, unicore_client.PathFile):
                with BytesIO() as in_memory_file:
                    val.download(in_memory_file)

                    try:
                        upload_url = bucket_wrapper.get_bucket_upload_url(bucket_name, os.path.basename(key),
                                                                          os.path.join(folder_path, results_dirname))
                    except CollabAccessError:
                        LOGGER.info(f'Could not upload file {key} to the selected Bucket. '
                                    f'You can find the results under the job directory.')
                        return
                    resp = requests.request("PUT", upload_url, data=in_memory_file.getvalue())
                    resp.raise_for_status()
                    LOGGER.info(f'File {key} has been stored to Bucket')


def get_xircuits_file():
    """
    :return: the file name and the absolute path for the compiled workflow file
    """
    # check that compiled .xircuits file is correctly passed as argument
    file_arg = sys.argv[1]
    LOGGER.info(f'Identified the executable file: {file_arg}')

    if os.path.exists(file_arg):
        full_path = os.path.abspath(file_arg)
    else:
        LOGGER.error(f"Cannot find the executable file: {file_arg}")
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
        LOGGER.error(f"Please provide the HPC project to run this job within, stopping execution.")
    else:
        workflow_name, workflow_path = get_xircuits_file()
        LOGGER.info("Preparing job...")
        files_to_upload = get_files_to_upload(xircuits_file_path=workflow_path)
        site_arg = sys.argv[2]
        project_arg = sys.argv[3]
        stage_out_arg = sys.argv[4]
        do_stage_out = True if stage_out_arg == 'true' else False
        launch_job(site=site_arg, project=project_arg, workflow_file_name=workflow_name,
                   workflow_file_path=workflow_path, files_to_upload=files_to_upload, do_stage_out=do_stage_out)

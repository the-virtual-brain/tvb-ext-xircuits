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
        return f'pip install -U pip && pip install {self.pip_libraries}'

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

    def submit_job(self, executable, inputs):
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
        else:
            print(f"Preparing environment in your {self.storage_name} folder...", flush=True)
            job_description = {
                self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._create_env_command} && "
                                     f"{self._activate_command} && {self._install_dependencies_command}",
                self.PROJECT_KEY: self.project,
                self.JOB_TYPE_KEY: self.INTERACTIVE_KEY}
            job = client.new_job(job_description, inputs=[])
            print(f"Job is running at {self.site}: {job.working_dir.properties['mountPoint']}. "
                  f"Submission time is: {self._format_date_for_job(job)}. "
                  f"It can be monitored with tvb-ext-unicore.", flush=True)
            job.poll()
            if job.properties['status'] == unicore_status.FAILED:
                print(f"Encountered an error during environment setup, stopping execution.")
                return
            print(f"Successfully finished the environment setup.")

        print("Launching workflow...", flush=True)
        job_description = {
            self.EXECUTABLE_KEY: f"{self._module_load_command} && {self._activate_command} && python {executable}",
            self.PROJECT_KEY: self.project}
        job1 = client.new_job(job_description, inputs=inputs)
        print(f"Job is running at {self.site}: {job1.working_dir.properties['mountPoint']}. "
              f"Submission time is: {self._format_date_for_job(job1)}.", flush=True)
        print('Finished remote launch. Please use tvb-ext-unicore to monitor it.', flush=True)


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


def launch_job(site, project, workflow_file_name, workflow_file_path, files_to_upload):
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

    PyunicoreSubmitter(site, project).submit_job(workflow_file_name, inputs)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(f"Please provide the HPC project to run this job within, stopping execution.")
    else:
        workflow_name, workflow_path = get_xircuits_file()
        print("Preparing job...", flush=True)
        files_to_upload = get_files_to_upload(xircuits_file_path=workflow_path)
        site_arg = sys.argv[2]
        project_arg = sys.argv[3]
        launch_job(site=site_arg, project=project_arg, workflow_file_name=workflow_name,
                   workflow_file_path=workflow_path, files_to_upload=files_to_upload)

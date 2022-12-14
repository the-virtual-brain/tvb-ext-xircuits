import os
import sys
import pyunicore.client as unicore_client
from pyunicore.credentials import AuthenticationFailedException
from tvbwidgets.core.auth import get_current_token

from xai_workflows.parse_files import get_files_to_upload


class PyunicoreSubmitter(object):
    storage_name = 'HOME'
    env_dir = 'tvb_xircuits'
    modules = 'cray-python'

    def __init__(self, site, project='ich012'):
        self.site = site
        self.project = project

    @property
    def _activate_command(self):
        return f'source ${self.storage_name}/{self.env_dir}/xircenv/bin/activate'

    @property
    def _module_load_command(self):
        return f'module load {self.modules}'

    @property
    def _create_env_command(self):
        return f'cd ${self.storage_name}/{self.env_dir} && rm -rf xircenv && python -mvenv xircenv'

    @property
    def _install_dependencies_command(self):
        return f'pip install -U pip && pip install tvb-ext-xircuits'

    def connect_client(self):
        os.environ['CLB_AUTH'] = ''
        print(f"Connecting to {self.site}...")
        token = get_current_token()
        transport = unicore_client.Transport(token)
        registry = unicore_client.Registry(transport, unicore_client._HBP_REGISTRY_URL)
        sites = registry.site_urls
        site_url = sites[self.site]
        try:
            client = unicore_client.Client(transport, site_url)
        except AuthenticationFailedException:
            print(f'Authentication to {self.site} failed, you might not have permissions to access it.', flush=True)
            return None

        print(f'Authenticated to {self.site} with success.', flush=True)
        return client

    def submit_job(self, executable, inputs):
        client = self.connect_client()

        print("Accessing storages...", flush=True)
        storages = client.get_storages(num=3)
        print(f"{storages}", flush=True)

        home_storage = storages[0]

        # print("Making dir...")
        # home_storage.mkdir(work_folder)

        print("Preparing env...", flush=True)
        job_description = {
            'Executable': f"{self._module_load_command} && {self._create_env_command} && {self._activate_command} && "
                          f"{self._install_dependencies_command}",
            'Project': self.project}
        job = client.new_job(job_description, inputs=[])
        print(job.working_dir.properties, flush=True)
        job.poll()

        print("Executing workflow...", flush=True)
        job_description = {
            'Executable': f"{self._module_load_command} && {self._activate_command} && python {executable}",
            'Project': self.project}
        job1 = client.new_job(job_description, inputs=inputs)
        print(job1.working_dir.properties, flush=True)

def get_xircuits_file():
    """
    :return: the file name and the absolute path for the compiled workflow file
    """
    # check that compiled .xircuits file is correctly passed as argument
    file_arg = sys.argv[-1]
    print(f'Identified the executable file: {file_arg}', flush=True)

    if os.path.exists(file_arg):
        full_path = os.path.abspath(file_arg)
    else:
        print("Cannot find " + file_arg)
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
    workflow_name, workflow_path = get_xircuits_file()
    print("Preparing job...", flush=True)
    files_to_upload = get_files_to_upload(xircuits_file_path=workflow_path)
    launch_job(site='DAINT-CSCS', project='', workflow_file_name=workflow_name, workflow_file_path=workflow_path,
               files_to_upload=files_to_upload)
    print('Job was launched. Monitor it using pyunicore', flush=True)


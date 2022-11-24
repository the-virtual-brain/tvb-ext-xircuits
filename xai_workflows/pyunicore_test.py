import os
import sys
import pyunicore
import pyunicore.client as unicore_client


def get_xircuits_file():
    """
    :return: the file name and the absolute path for the compiled workflow file
    """
    # check that compiled .xircuits file is correctly passed as argument
    file_arg = sys.argv[-1]
    print(f'THIS IS THE FILE: {file_arg}')

    if os.path.exists(file_arg):
        full_path = os.path.abspath(file_arg)
        print(full_path)
    else:
        print("Cannot find " + file_arg)
        full_path = None

    filename = os.path.basename(file_arg)
    print(f'JUST FILE NAME: {filename}')

    return filename, full_path


def get_unicore_client():
    """
    :return: pyunicore client to access EBRAINS sites
    """

    # check correct verion for pyunicore
    print(f'pyunicore version: {pyunicore.__version__}')

    # set ebrains token
    token = ''

    # get available sites and create client for the site
    transport = unicore_client.Transport(token)
    # sites = unicore_client.get_sites(transport)
    # site_url = sites['JUDAC']  # change 'JUSUF' to 'JUDAC' or DAINT-CSCS
    # client = unicore_client.Client(transport, site_url)
    registry = unicore_client.Registry(transport, unicore_client._HBP_REGISTRY_URL)
    sites = registry.site_urls
    site_url = sites['JUSUF']  # change 'JUSUF' to 'JUDAC' or DAINT-CSCS
    client = unicore_client.Client(transport, site_url)

    return client


def launch_job(client, workflow_file_name, workflow_file_path):
    """
    Submit a job to a EBRAINS HPC site
    :param client: unicore client to connect to site
    :param workflow_file_name: base name of compiled workflow file
    :param workflow_file_path: absolute path of compiled workflow file
    :return: None
    """
    # create dummy job
    # job_description = {'Executable': 'date'}
    job_description = {
        # "Executable": f"python3 {workflow_file_name}"
        "Executable": f"python3 test1.py"
    }

    # submit job
    # job = client.new_job(job_description, inputs=[workflow_file_path])
    job = client.new_job(job_description, inputs=['/Users/pipeline/WORK/TVB_GIT/tvb-ext-xircuits/xai_workflows/test1.py'])
    print(job)


if __name__ == '__main__':
    workflow_name, workflow_path = get_xircuits_file()
    client = get_unicore_client()
    launch_job(client=client, workflow_file_name=workflow_name, workflow_file_path=workflow_path)

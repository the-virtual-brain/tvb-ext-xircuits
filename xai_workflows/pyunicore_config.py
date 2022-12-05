import os
import sys
import pyunicore.client as unicore_client
from pyunicore.credentials import AuthenticationFailedException
from xai_workflows.parse_files import get_files_to_upload


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


def get_unicore_client():
    """
    :return: pyunicore client to access EBRAINS sites
    """

    # check correct verion for pyunicore
    # print(f'pyunicore version: {pyunicore.__version__}')

    # set ebrains token
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfNkZVSHFaSDNIRmVhS0pEZDhXcUx6LWFlZ3kzYXFodVNJZ1RXaTA1U2k0In0.eyJleHAiOjE2NzA4MzE2OTYsImlhdCI6MTY3MDIyNzA4MCwiYXV0aF90aW1lIjoxNjcwMjI2ODk2LCJqdGkiOiI2YTBlMDlkMS1hNGJhLTQ2MzctYjVkYS1iNDk1MTg5ZGRiMzQiLCJpc3MiOiJodHRwczovL2lhbS5lYnJhaW5zLmV1L2F1dGgvcmVhbG1zL2hicCIsInN1YiI6ImIyNTdjNGUxLTA5NjUtNDkxNi04M2EzLTQ0ZTJkYmQ2NTVhYyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImtnLW5leHVzLXNlcnZpY2UiLCJzZXNzaW9uX3N0YXRlIjoiNTNlNGU5MDItMjg5OC00OWM0LTlkNjItZGI1NDE1YjdkNjEwIiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL25leHVzLWlhbS5odW1hbmJyYWlucHJvamVjdC5vcmciLCJodHRwczovL25leHVzLWlhbS1pbnQuaHVtYW5icmFpbnByb2plY3Qub3JnIl0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCBvcGVuaWQgZ3JvdXAgY2xiLndpa2kucmVhZCIsInNpZCI6IjUzZTRlOTAyLTI4OTgtNDljNC05ZDYyLWRiNTQxNWI3ZDYxMCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiUm9taW5hIEJhaWxhIiwibWl0cmVpZC1zdWIiOiI0MzcyNTIzMzk3NjU1NzI3IiwicHJlZmVycmVkX3VzZXJuYW1lIjoicm9taW5hYmFpbGEiLCJnaXZlbl9uYW1lIjoiUm9taW5hIiwiZmFtaWx5X25hbWUiOiJCYWlsYSIsImVtYWlsIjoicm9taW5hLmJhaWxhQGNvZGVtYXJ0LnJvIn0.B5MAZZEGdngL2SItw0-LOnTTY08TJMW0Ak5BDCm_-T49IZ9mcXSBsfSnXVH9JZg7Y1niZvnedhEGSjJss_Isk5PczsBEDBRGH9ZOzNwr5envSOsBLAoVKJQS3JNljtx_MjkO8m0EMHZ1yYeyl5BlLopeNYwjiABFRvmaKl_XnfNduSPgRt_HZcG9BkvbbcgS7vlRVReZmwJDo7tOW5EFOXvkLlerlmpluKF08oVz9XfggC190n9hGJhFkETIRdGxJ-DAswMuStBSBM9y7EFZrTVp7Ng5UCCvNlNEu5jOrUhlMb5iPJWs_Y2Nrez1yx7GDWEvabrNdkTefkNKPZcaeA'
    site = 'JUSUF'
    print(f'Authenticating to {site}...')

    # get available sites and create client for the site
    transport = unicore_client.Transport(token)
    registry = unicore_client.Registry(transport, unicore_client._HBP_REGISTRY_URL)
    sites = registry.site_urls
    site_url = sites[site]  # change 'JUSUF' to 'JUDAC' or DAINT-CSCS
    try:
        client = unicore_client.Client(transport, site_url)
    except AuthenticationFailedException:
        print(f'Authentication to {site} failed, you might not have permissions to access it.', flush=True)
        return None

    print(f'Authenticated to {site} with success.', flush=True)
    return client


def launch_job(client, workflow_file_name, workflow_file_path, files_to_upload):
    """
    Submit a job to a EBRAINS HPC site
    :param client: unicore client to connect to site
    :param workflow_file_name: base name of compiled workflow file
    :param workflow_file_path: absolute path of compiled workflow file
    :param files_to_upload: list of additional files that need to be sent to the HPC server
    :return: None
    """
    inputs = [workflow_file_path]
    if files_to_upload:
        inputs.extend(files_to_upload)
    # create job
    job_description = {
        "Executable": f"python3 {workflow_file_name}"
        # "Executable": f"python3 test1.py"
    }

    # submit job
    job = client.new_job(job_description, inputs=inputs)
    # job = client.new_job(job_description, inputs=['C:\\Work\\TVB\\tvb-ext-xircuits\\xai_workflows\\test1.py'])
    print(job)


if __name__ == '__main__':
    workflow_name, workflow_path = get_xircuits_file()
    client = get_unicore_client()
    if client:
        print("Executing job...", flush=True)
        files_to_upload = get_files_to_upload()
        launch_job(client=client, workflow_file_name=workflow_name, workflow_file_path=workflow_path,
                   files_to_upload=files_to_upload)
    print('Job was launched. Monitor it using pyunicore', flush=True)


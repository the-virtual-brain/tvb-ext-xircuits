import filecmp
from pathlib import Path

STORAGE_CONFIG_FILE = 'storage_config.json'  # To be used only for HPC runs
COLLAB_NAME_KEY = 'collab_name'  # Used only for HPC runs
BUCKET_NAME_KEY = 'bucket_name'  # Used only for HPC runs
FOLDER_PATH_KEY = 'folder_path'  # Used only for HPC runs
STORE_RESULTS_DIR = 'results'  # Used by component that takes care of storing data and stage-out from HPC
DIR_TIME_STAMP_FRMT = '%Y.%m.%d_%H_%M_%S'

import os
import urllib.parse
import shutil
import importlib_resources

def is_empty(directory):
    # will return true for uninitialized submodules
    return not os.path.exists(directory) or not os.listdir(directory)

def is_valid_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def are_folders_identical(resource_path, dest_path):
    """
    Check if two folders are identical.
    """
    comparison_dir = filecmp.dircmp(resource_path, dest_path)
    return not (comparison_dir.left_only or comparison_dir.right_only or comparison_dir.diff_files)

def copy_from_installed_wheel(package_name, resource="", dest_path=None):
    if dest_path is None:
        dest_path = package_name

    # Get the resource reference
    ref = importlib_resources.files(package_name) / resource

    config_path = Path(os.getcwd()) / dest_path
    # Create the temporary file context
    with importlib_resources.as_file(ref) as resource_path:
        if config_path.exists() and not are_folders_identical(resource_path, dest_path):
            shutil.rmtree(config_path)
            shutil.copytree(resource_path, dest_path, dirs_exist_ok=True)
        elif not config_path.exists():
            shutil.copytree(resource_path, dest_path)
import json
from pathlib import Path

from jupyter_core.paths import jupyter_config_dir

from tvbextxircuits.logger.builder import get_logger

STORAGE_CONFIG_FILE = 'storage_config.json'  # To be used only for HPC runs
COLLAB_NAME_KEY = 'collab_name'  # Used only for HPC runs
BUCKET_NAME_KEY = 'bucket_name'  # Used only for HPC runs
FOLDER_PATH_KEY = 'folder_path'  # Used only for HPC runs
STORE_RESULTS_DIR = 'results'  # Used by component that takes care of storing data and stage-out from HPC
DIR_TIME_STAMP_FRMT = '%Y.%m.%d_%H_%M_%S'

LOGGER = get_logger(__name__)

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

def copy_from_installed_wheel(package_name, resource="", dest_path=None, version_changed=False):
    if dest_path is None:
        dest_path = package_name

    # Get the resource reference
    ref = importlib_resources.files(package_name) / resource

    config_path = Path(os.getcwd()) / dest_path
    # Create the temporary file context
    with importlib_resources.as_file(ref) as resource_path:
        dest_path_abs = os.path.abspath(dest_path)
        if str(resource_path) != dest_path_abs:
            if not config_path.exists() or version_changed:
                if config_path.exists():
                    shutil.rmtree(config_path)
                shutil.copytree(resource_path, dest_path)


def get_user_settings():
    data_dir = jupyter_config_dir()   # path to jupyter configs folder; usually it's $HOME/.jupyter
    # path to user-settings for this extension
    settings_path = os.path.join(data_dir, 'lab', 'user-settings', 'tvb-ext-xircuits', 'settings.jupyterlab-settings')
    if os.path.exists(settings_path):
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    else:
        settings = {}

    return settings


def get_base_dir_web():
    user_settings = get_user_settings()
    base_dir = user_settings.get('baseDirectoryWeb', '.')  # if baseDirectory is not set, use a default value
    LOGGER.info(f'Base directory Web in user settings is: {base_dir}')
    base_dir = os.path.abspath(os.path.expanduser(base_dir))
    return base_dir


def get_base_dir_kernel():
    user_settings = get_user_settings()
    base_dir = user_settings.get('baseDirectoryKernel', '.')  # if baseDirectory is not set, use a default value
    LOGGER.info(f'Base directory Kernel in user settings is: {base_dir}')
    base_dir = os.path.abspath(os.path.expanduser(base_dir))
    return base_dir

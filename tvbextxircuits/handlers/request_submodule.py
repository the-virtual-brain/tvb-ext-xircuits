import os
from git import Repo
from git.remote import RemoteProgress
from pathlib import Path

from tvbextxircuits.logger.builder import get_logger

LOGGER = get_logger(__name__)


class Progress(RemoteProgress):
    def update(self, *args):
        LOGGER.info(self._cur_line, end='\r')

def get_submodule_config(user_query):
    
    import configparser
    config = configparser.ConfigParser()
    
    config.read('.xircuits/.gitmodules')
    
    submodule_keys = [submodule for submodule in config.sections() if user_query in submodule]
    if len(submodule_keys) == 0:
        LOGGER.warn(user_query + " component library submodule not found.")
        return
        
    if len(submodule_keys) > 1:
        LOGGER.warn("Multiple '" + user_query + "' found. Returning first instance.")

    submodule_key = submodule_keys.pop(0)
    
    submodule_path = config[submodule_key]["path"]
    submodule_url = config[submodule_key]["url"]
    
    return submodule_path, submodule_url


def request_submodule_library(component_library_query):

    # ensure syntax is as xai_components/xai_library_name
    if "xai" not in component_library_query:
        component_library_query = "xai_" + component_library_query

    if "xai_components" not in component_library_query:
        component_library_query = "xai_components/" + component_library_query
    
    submodule_path, submodule_url = get_submodule_config(component_library_query)
    
    LOGGER.info("Cloning " + submodule_path + " from " + submodule_url)
    Repo.clone_from(submodule_url, submodule_path, progress=Progress())

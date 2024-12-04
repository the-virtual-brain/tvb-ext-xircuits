import argparse
import importlib.metadata
from pathlib import Path
import os
from .utils import is_empty, copy_from_installed_wheel
from .library import list_component_library, install_library, fetch_library, save_component_library_config
from .compiler import compile
import json

from .logger.builder import get_logger

LOGGER = get_logger(__name__)

def init_xircuits(vers_changed=False):
    package_name = 'tvbextxircuits'
    copy_from_installed_wheel(package_name, resource='.xircuits', dest_path='.xircuits', version_changed=vers_changed)
    copy_from_installed_wheel('xai_components', '', 'xai_components', version_changed=vers_changed)

    # Create a version file for keeping generated folders in sync after a new release is installed
    try:
        version_file = Path(os.getcwd()) / '.version'
        current_version = get_extension_version()
        version_file.write_text(current_version)
        LOGGER.info("Create version file.")
    except Exception as e:
        LOGGER.error(f"Error handling version file: {e}")


def version_changed():
    """
    Compares user's current version with the version installed on lab.
    If they differ, a new version is available.
    """
    version_file = Path(os.getcwd()) / '.version'
    running_version = get_extension_version()

    if not running_version:
        LOGGER.error("Not able to retrieve the installed version.")
        return

    if not version_file.exists():
        LOGGER.info("Version file not found.")
        return True

    try:
        stored_version = version_file.read_text().strip()
    except Exception as e:
        LOGGER.error(f"Error reading version file: {e}")
        stored_version = None

    return stored_version != running_version

def get_extension_version():
    """
    Retrieves current version of the package
    """
    try:
        version = importlib.metadata.version("tvb-ext-xircuits")
        return version
    except importlib.metadata.PackageNotFoundError:
        LOGGER.error("Package 'tvb-ext-xircuits' is not installed.")
        return None


def cmd_start_xircuits(args, extra_args=[]):
    # fetch xai_components
    component_library_path = Path(os.getcwd()) / "xai_components"
    if not component_library_path.exists():
        copy_from_installed_wheel('xai_components', '', 'xai_components')

    news_url_option = '--LabApp.news_url="https://xpress.ai/blog/atom.xml"'

    # handler for extra jupyterlab launch options
    if extra_args:
        try:
            launch_cmd = "jupyter lab --ContentsManager.allow_hidden=True" + " " + " ".join(extra_args) + " " + news_url_option
            os.system(launch_cmd)
        except Exception as e:
            LOGGER.error("Error in launch args! Error log:\n")
            LOGGER.error(e)
    else:
        os.system(f"jupyter lab --ContentsManager.allow_hidden=True {news_url_option}")

def cmd_download_examples(args, extra_args=[]):
    if not os.path.exists("examples") or is_empty("examples"):
        copy_from_installed_wheel('examples')
        LOGGER.info("Example workflows ready at working directory.")

def cmd_fetch_library(args, extra_args=[]):
    fetch_library(args.library_name)

def cmd_install_library(args, extra_args=[]):
    install_library(args.library_name)

def cmd_compile(args, extra_args=[]):
    component_paths = {}
    if args.python_paths_file:
        component_paths = json.load(args.python_paths_file)
    compile(args.source_file, args.out_file, component_python_paths=component_paths)

def cmd_list_libraries(args, extra_args=[]):
    list_component_library()

def main():
    parser = argparse.ArgumentParser(description='Xircuits Command Line Interface', add_help=False)
    subparsers = parser.add_subparsers(dest="command")

# Adding parser for 'start' command
    start_parser = subparsers.add_parser('start', help='Start Xircuits.')
    # Add an arbitrary list of arguments. The nargs="*" means 0 or more arguments.
    # This will collect all additional arguments into a list.
    start_parser.add_argument('extra_args', nargs='*', help='Additional arguments for Xircuits launch command')
    start_parser.set_defaults(func=cmd_start_xircuits)

    # Adding parser for 'install' command
    install_parser = subparsers.add_parser('install', help='Fetch and installs a library for Xircuits.')
    install_parser.add_argument('library_name', type=str, help='Name of the library to install')
    install_parser.set_defaults(func=cmd_install_library)

    # Adding parser for 'fetch' command
    fetch_parser = subparsers.add_parser('fetch-only', help='Fetch a library for Xircuits. Does not install.')
    fetch_parser.add_argument('library_name', type=str, help='Name of the library to fetch')
    fetch_parser.set_defaults(func=cmd_fetch_library)

    # Adding parser for 'examples' command
    examples_parser = subparsers.add_parser('examples', help='Get example workflows for Xircuits.')
    examples_parser.add_argument('--branch', nargs='?', default="master", help='Load example workflows to current working directory/')
    examples_parser.set_defaults(func=cmd_download_examples)

    # Adding parser for 'compile' command
    compile_parser = subparsers.add_parser('compile', help='Compile a Xircuits workflow file.')
    compile_parser.add_argument('source_file', type=argparse.FileType('r', encoding='utf-8'))
    compile_parser.add_argument('out_file', type=argparse.FileType('w', encoding='utf-8'))
    compile_parser.add_argument("python_paths_file", nargs='?', default=None, type=argparse.FileType('r'),
                                help="JSON file with a mapping of component name to required python path. "
                                     "e.g. {'MyComponent': '/some/path'}")
    compile_parser.set_defaults(func=cmd_compile)

    # Adding parser for 'list' command
    list_parser = subparsers.add_parser('list', help='List available component libraries for Xircuits.')
    list_parser.set_defaults(func=cmd_list_libraries)

    args, unknown_args = parser.parse_known_args()

    if hasattr(args, 'func'):
        args.func(args, unknown_args)
    else:
        valid_help_args = {"-h", "--h" "-help", "--help"}
        if any(arg in unknown_args for arg in valid_help_args):
            parser.print_help()
        else:
            # Default behavior: if no sub-command is provided, start xircuits.
            cmd_start_xircuits(args, unknown_args)

    return 0

def init_configs():
    LOGGER.info(
        '''
        ======================================
        __   __  ___                _ _       
        \ \  \ \/ (_)_ __ ___ _   _(_) |_ ___ 
         \ \  \  /| | '__/ __| | | | | __/ __|
         / /  /  \| | | | (__| |_| | | |_\__ \\
        /_/  /_/\_\_|_|  \___|\__,_|_|\__|___/

        ======================================
        '''
    )
    vers_changed = version_changed()
    config_path = Path(os.getcwd()) / ".xircuits"
    if not config_path.exists() or vers_changed:
        init_xircuits(vers_changed)

    save_component_library_config()


if __name__ == '__main__':
    main()

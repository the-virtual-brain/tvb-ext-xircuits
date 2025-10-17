import os
import configparser

from tvbextxircuits.logger.builder import get_logger

LOGGER = get_logger(__name__)


def is_on_hub() -> bool:
    """
    Detect whether the extension is running in a JupyterHub environment (e.g., JSC).
    We check for 'JUPYTERHUB_API_TOKEN', which is typically only set in JupyterHub.
    Note: In the future we might want to do this smarter.
    """
    return bool(os.getenv('JUPYTERHUB_API_TOKEN'))

def is_on_ebrains() -> bool:
    """
    Detect whether the extension is running at EBrains lab.
    We check for clb_nb_utils module.
    """
    try:
        from clb_nb_utils import oauth as clb_oauth
        return callable(getattr(clb_oauth, "get_token", None))
    except ImportError:
        return False



def load_settings() -> dict[str, str]:
    """
    Load settings from the appropriate config file based on environment.
    - JupyterHub: loads 'settings.hub.conf'
    - Local: loads 'settings.local.conf'
    """
    config = configparser.ConfigParser()
    filename = 'settings.hub.conf' if is_on_hub() and not is_on_ebrains() else 'settings.local.conf'
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', filename))

    if not os.path.exists(config_path):
        LOGGER.error(f'Settings file not found: {config_path}')
        return {}

    config.read(config_path)
    return dict(config['defaults'])


settings_config = load_settings()

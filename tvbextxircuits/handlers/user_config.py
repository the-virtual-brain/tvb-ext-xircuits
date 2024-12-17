import json
from pathlib import Path
import tornado
from jupyter_server.base.handlers import APIHandler
import os

from tvbextxircuits.logger.builder import get_logger
from tvbextxircuits.nb_generator import IS_WINDOWS
from tvbextxircuits.utils import get_base_dir_web, get_base_dir_kernel

LOGGER = get_logger(__name__)


class HomeDirectoryHandler(APIHandler):

    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({"data": "This is /config/home_directory endpoint!"}))

    @tornado.web.authenticated
    def post(self):
        # get user's home directory
        input_data = self.get_json_body()

        try:
            path = input_data["node_path"]
            LOGGER.info(f'Component script path is: {path}')

            if IS_WINDOWS:
                self.finish(json.dumps({"homeDirectory": path}))
            else:
                base_dir_web = get_base_dir_web()
                home_directory = os.path.join(base_dir_web, path)
                base_dir_kernel = get_base_dir_kernel()
                return_path = str(Path(home_directory).relative_to(Path(base_dir_kernel)))
                LOGGER.info(f'Opening component script from path: {return_path}')
                self.finish(json.dumps({"homeDirectory": return_path}))
        except KeyError:
            data = {"error_msg": "Could not determine path from POST params!"}
            self.finish(json.dumps(data))
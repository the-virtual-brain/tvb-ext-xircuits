import json
import tornado
from jupyter_server.base.handlers import APIHandler
import os
from tvbextxircuits.nb_generator import IS_WINDOWS


class HomeDirectoryHandler(APIHandler):

    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({"data": "This is /config/home_directory endpoint!"}))

    @tornado.web.authenticated
    def post(self):
        # get user's home directory
        input_data = self.get_json_body()

        try:
            # TODO: temporary hack for debug purposes on juwels, also handle the other operating systems(not just
            #  windows)
            path = input_data["node_path"]
            if IS_WINDOWS:
                self.finish(json.dumps({"homeDirectory": path}))
            else:
                home_directory = os.path.expanduser(os.path.join('~', path))
                self.finish(json.dumps({"homeDirectory": home_directory}))
        except KeyError:
            data = {"error_msg": "Could not determine path from POST params!"}
            self.finish(json.dumps(data))
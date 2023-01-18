import json
import tornado
from jupyter_server.base.handlers import APIHandler
from .component_parser import ComponentsParser
from tvbextxircuits.nb_generator import ModelConfigLoader, NotebookFactory


class EditXircuitsFile(APIHandler):
    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        xircuits_id = None

        try:
            xircuits_id = input_data["xircuits_id"]
        except KeyError:
            data = {"models_exist": False, "error_msg": "Could not determine the Xircuits ID from POST params!"}
            self.finish(json.dumps(data))

        model_config_loader = ModelConfigLoader(xircuits_id)
        result = model_config_loader.load_configs()

        if result is False:
            data = {"models_exist": False}

        else:
            data = {"models_exist": True,
                    "models": result
                    }

        self.finish(json.dumps(data))


class ComponentsRouteHandler(APIHandler):
    component_parser = ComponentsParser()

    @tornado.web.authenticated
    def get(self):
        self.finish(self.component_parser.get())

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()

        try:
            component = input_data["component"]
            component_id = input_data["component_id"]
            component_path = input_data["path"]
            xircuits_id = input_data["xircuits_id"]
            component_inputs = input_data['component_inputs']

            notebook_path = self._generate_widget_notebook(component, component_id, component_path, xircuits_id,
                                                           component_inputs)
            data = {"widget": notebook_path}
            self.finish(json.dumps(data))

        except KeyError:
            data = {"error_msg": "Could not determine the component from POST params!"}
            self.finish(json.dumps(data))

    def _generate_widget_notebook(self, component, component_id, component_path, xircuits_id, component_inputs):
        factory = NotebookFactory()
        notebook = factory.get_notebook_for_component(component, component_id, component_path, component_inputs)
        path = factory.store(notebook, component, xircuits_id)
        return path

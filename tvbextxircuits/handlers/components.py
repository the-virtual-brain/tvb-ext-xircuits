import json
import tornado
from jupyter_server.base.handlers import APIHandler
from .component_parser import ComponentsParser
from tvbextxircuits.nb_generator import NotebookGenerator, WidgetCodeGenerator, ModelConfigLoader

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

            notebook_path = self.generate_widget_notebook(component, component_id, component_path, xircuits_id)
            data = {"widget": notebook_path}
            self.finish(json.dumps(data))

        except KeyError:
            data = {"error_msg": "Could not determine the component from POST params!"}
            self.finish(json.dumps(data))

    def generate_widget_notebook(self, component, component_id, component_path, xircuits_id):
        nb_generator = NotebookGenerator()

        text = f"""# Interactive setup for {component} model"""
        nb_generator.add_markdown_cell(text)
        text = f"#### Run the cell below in order to display the Phase Plane\n" \
               f"#### Export the model configuration to add it in the Xircuits diagram\n" \
               f"*Some select fields in the Phase Plane are meant to be disabled in this context"
        nb_generator.add_markdown_cell(text)
        nb_generator.add_code_cell(WidgetCodeGenerator.get_widget_code(component, component_id, component_path))

        path = nb_generator.store(component, xircuits_id)
        return path


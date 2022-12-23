# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import importlib
import json
import os
import nbformat
from tvb.simulator.integrators import HeunDeterministic
from tvb.simulator.models.oscillator import Generic2dOscillator

from xai_components.base_tvb import ComponentWithWidget

NOTEBOOKS_DIR = 'TVB_generated_notebooks'
MODEL_CONFIG_FILE_PREFIX = 'model'


class ModelConfigLoader(object):

    def __init__(self, xircuits_id):
        self.model_configs_folder = os.path.join(NOTEBOOKS_DIR, xircuits_id)

    def load_configs(self):
        all_model_config_files = self._find_model_config_files()

        if all_model_config_files is False:
            return False

        json_result = dict()
        for filename in all_model_config_files:
            json_entry = self._read_model_config_file(filename)
            json_result.update(json_entry)
            self._remove_file(filename)

        return json_result

    def _find_model_config_files(self):
        if not os.path.exists(self.model_configs_folder):
            return False

        all_files = os.listdir(self.model_configs_folder)
        all_model_config_files = [file for file in all_files if file.startswith(MODEL_CONFIG_FILE_PREFIX)]

        if len(all_model_config_files) == 0:
            return False

        return all_model_config_files

    def _read_model_config_file(self, filename):
        # TODO: better processing of filename
        model_id = filename[len(MODEL_CONFIG_FILE_PREFIX) + 1:].split('.')[0]

        model_name = 'model'
        model_params_json = dict()
        with open(os.path.join(self.model_configs_folder, filename)) as f:
            model_config_json = json.load(f)
            for param_name, param_val in list(model_config_json.values())[0].items():
                if param_name == 'model':
                    model_name = param_val
                    continue
                param_entry = {
                    param_name: {'name': param_name, 'value': param_val[0], 'type': type(param_val[0]).__name__}}
                model_params_json.update(param_entry)

        return {
            model_name: {
                "id": model_id,
                "params": model_params_json
            }
        }

    def _remove_file(self, filename):
        os.remove(os.path.join(self.model_configs_folder, filename))
        if len(os.listdir(self.model_configs_folder)) == 0:
            os.rmdir(self.model_configs_folder)


class NotebookGenerator(object):

    def __init__(self):
        if not os.path.exists(NOTEBOOKS_DIR):
            os.mkdir(NOTEBOOKS_DIR)

        self.notebook = nbformat.v4.new_notebook()

    def add_code_cell(self, code):
        self._add_cell(nbformat.v4.new_code_cell(code, metadata={'editable': False, 'deletable': False}))

    def add_markdown_cell(self, text):
        self._add_cell(nbformat.v4.new_markdown_cell(text))

    def _add_cell(self, cell):
        self.notebook['cells'].append(cell)

    def store(self, component, xircuits_id):
        file_name = f'{component}_widget.ipynb'

        notebook_dir = os.path.join(NOTEBOOKS_DIR, xircuits_id)
        if not os.path.exists(notebook_dir):
            os.mkdir(notebook_dir)

        path = os.path.join(notebook_dir, file_name)

        with open(path, 'w') as f:
            nbformat.write(self.notebook, f)

        return os.path.join(notebook_dir, file_name)


class WidgetCodeGenerator(object):

    @staticmethod
    def phase_plane(model=Generic2dOscillator, integrator=HeunDeterministic, export_filename=None):
        code = "%matplotlib widget\n" \
               "\n" \
               "from tvb.simulator.lab import models, integrators\n" \
               "from tvbwidgets.api import PhasePlaneWidget\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "w = PhasePlaneWidget(model=models.{0}(), integrator=integrators.{1}());\n" \
               "w.export_filename = '{2}' \n" \
               "w.disable_model_dropdown = True \n" \
               "w.disable_export_dropdown = True \n" \
               "display(w.get_widget());"
        return code.format(model.__name__, integrator.__name__, export_filename)

    @staticmethod
    def get_widget_code(component_name, component_id, component_path):
        component_class = determine_component_class(component_name, component_path)

        if issubclass(component_class, ComponentWithWidget):
            return WidgetCodeGenerator.phase_plane(component_class().tvb_ht_class,
                                                   export_filename=f"{MODEL_CONFIG_FILE_PREFIX}_{component_id}")

        else:
            return None


def determine_component_class(component_name, component_path):
    component_module = importlib.import_module(component_path.replace('/', '.')[:-3])
    component_class = getattr(component_module, component_name)
    return component_class

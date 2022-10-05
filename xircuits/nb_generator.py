# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import importlib
import os
import nbformat
from tvb.simulator.integrators import HeunDeterministic
from tvb.simulator.models.oscillator import Generic2dOscillator

from xai_components.base_tvb import ComponentWithWidget

NOTEBOOKS_DIR = 'TVB_generated_notebooks'
MODEL_CONFIG_FILE_PREFIX = 'model'


class ModelConfigLoader(object):

    def load_configs(self):
        all_model_config_files = self._find_model_config_files()

        if all_model_config_files is False:
            return False

        json_result = {}
        for filename in all_model_config_files:
            json_entry = self._read_model_config_file(filename)
            json_result.update(json_entry)
            self._remove_file(filename)

        return json_result

    def _find_model_config_files(self):
        if not os.path.exists(NOTEBOOKS_DIR):
            return False

        all_files = os.listdir(NOTEBOOKS_DIR)
        all_model_config_files = [file for file in all_files if file.startswith(MODEL_CONFIG_FILE_PREFIX)]

        if len(all_model_config_files) == 0:
            return False

        return all_model_config_files

    def _read_model_config_file(self, filename):
        # TODO: better processing of filename
        model_id = filename[len(MODEL_CONFIG_FILE_PREFIX) + 1:].split('.')[0]
        # TODO: read contents of file (JSON or PY? both?)
        return {
            "model": {
                "id": model_id,
                "params": {
                    "tau": {"name": "tau", "value": "3.97", "type": "float"},
                    "J": {"name": "J", "value": "4.01", "type": "float"}
                }
            }
        }

    def _remove_file(self, filename):
        os.remove(os.path.join(NOTEBOOKS_DIR, filename))


class NotebookGenerator(object):

    def __init__(self):
        if not os.path.exists(NOTEBOOKS_DIR):
            os.mkdir(NOTEBOOKS_DIR)

        self.notebook = nbformat.v4.new_notebook()

    def add_code_cell(self, code):
        self._add_cell(nbformat.v4.new_code_cell(code))

    def add_markdown_cell(self, text):
        self._add_cell(nbformat.v4.new_markdown_cell(text))

    def _add_cell(self, cell):
        self.notebook['cells'].append(cell)

    def store(self, component):
        file_name = f'{component}_widget.ipynb'
        path = os.path.join(NOTEBOOKS_DIR, file_name)

        with open(path, 'w') as f:
            nbformat.write(self.notebook, f)

        return os.path.join(os.path.basename(os.path.dirname(path)), file_name)


class WidgetCodeGenerator(object):

    @staticmethod
    def phase_plane(model=Generic2dOscillator, integrator=HeunDeterministic, export_filename=None):
        code = "from tvb.simulator.lab import models, integrators\n" \
               "from tvbwidgets.api import PhasePlaneWidget\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "w = PhasePlaneWidget(model=models.{0}(), integrator=integrators.{1}());\n" \
               "w.export_filename = '{2}' \n" \
               "display(w.get_widget());"
        return code.format(model.__name__, integrator.__name__, export_filename)

    @staticmethod
    def get_widget_code(component_name, component_id, component_path):
        component_class = determine_component_class(component_name, component_path)

        if issubclass(component_class, ComponentWithWidget):
            return WidgetCodeGenerator.phase_plane(component_class().tvb_ht_class,
                                                   export_filename=f"{MODEL_CONFIG_FILE_PREFIX}_{component_id}")

        else:
            return WidgetCodeGenerator.phase_plane()


def determine_component_class(component_name, component_path):
    component_module = importlib.import_module(component_path.replace(os.sep, '.')[:-3])
    component_class = getattr(component_module, component_name)
    return component_class

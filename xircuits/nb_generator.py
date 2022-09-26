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


class NotebookGenerator(object):

    def __init__(self, notebooks_dir=None):
        if notebooks_dir is None:
            notebooks_dir = 'TVB_generated_notebooks'

        if not os.path.exists(notebooks_dir):
            os.mkdir(notebooks_dir)

        self.notebooks_dir = notebooks_dir
        self.notebook = nbformat.v4.new_notebook()

    def add_code_cell(self, code):
        self._add_cell(nbformat.v4.new_code_cell(code))

    def add_markdown_cell(self, text):
        self._add_cell(nbformat.v4.new_markdown_cell(text))

    def _add_cell(self, cell):
        self.notebook['cells'].append(cell)

    def store(self, component):
        file_name = f'{component}_widget.ipynb'
        path = os.path.join(self.notebooks_dir, file_name)

        with open(path, 'w') as f:
            nbformat.write(self.notebook, f)

        return os.path.join(os.path.basename(os.path.dirname(path)), file_name)


class WidgetCodeGenerator(object):

    @staticmethod
    def phase_plane(model=Generic2dOscillator, integrator=HeunDeterministic):
        code = "from tvb.simulator.lab import models, integrators\n" \
               "from tvbwidgets.api import PhasePlaneWidget\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "w = PhasePlaneWidget(model=models.{0}(), integrator=integrators.{1}());\n" \
               "display(w.get_widget());"
        return code.format(model.__name__, integrator.__name__)

    @staticmethod
    def get_widget_code(component_name, component_path):
        component_class = determine_component_class(component_name, component_path)

        if issubclass(component_class, ComponentWithWidget):
            return WidgetCodeGenerator.phase_plane(component_class().tvb_ht_class)

        else:
            return WidgetCodeGenerator.phase_plane()


def determine_component_class(component_name, component_path):
    component_module = importlib.import_module(component_path.replace(os.sep, '.')[:-3])
    component_class = getattr(component_module, component_name)
    return component_class

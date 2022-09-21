import os
import nbformat

from xai_components.xai_tvb.showcase1 import MontbrioPazoRoxinModelComponent
from xai_components.xai_tvb.simulator_code import Generic2dOscillatorComponent


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

    # TODO: keep strings here? Or use TVB classes?
    @staticmethod
    def phase_plane(model='Generic2dOscillator', integrator='HeunDeterministic'):
        code = "from tvb.simulator.lab import models, integrators\n" \
               "from tvbwidgets.api import PhasePlaneWidget\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "w = PhasePlaneWidget(model=models.{0}(), integrator=integrators.{1}());\n" \
               "display(w.get_widget());"
        return code.format(model, integrator)

    @staticmethod
    def get_widget_code(component_name):
        # TODO: how to determine which components use the PPW?
        tvb_ht_name = component_name

        suffixes = ['ModelComponent', 'Component']
        for suffix in suffixes:
            if tvb_ht_name.endswith(suffix):
                tvb_ht_name = component_name[:-len(suffix)]

        if component_name in [Generic2dOscillatorComponent.__name__, MontbrioPazoRoxinModelComponent.__name__]:
            return WidgetCodeGenerator.phase_plane(tvb_ht_name)

        else:
            return WidgetCodeGenerator.phase_plane()

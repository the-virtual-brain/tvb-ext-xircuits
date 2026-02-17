# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import json
import os
import sys
import nbformat
import importlib
from tvb.simulator.integrators import HeunDeterministic
from tvb.simulator.models.oscillator import Generic2dOscillator

from tvbextxircuits.utils import get_base_dir_web, get_base_dir_kernel
from xai_components.base_tvb import ComponentWithWidget, ComponentWithViewer

from xai_components.logger.builder import get_logger
from pathlib import Path

LOGGER = get_logger(__name__)
IS_WINDOWS = sys.platform.startswith('win')
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


class NotebookFactory(object):

    @staticmethod
    def get_notebook_for_component(component_name, component_id, component_path, component_inputs, xircuits_id, xircuits_filename):
        component_class = determine_component_class(component_name, component_path)

        if not (issubclass(component_class, ComponentWithWidget) or issubclass(component_class, ComponentWithViewer)):
            return None

        if component_class.__name__.startswith('StoreResults'):
            return TimeSeriesNotebookGenerator(component_class, component_id, component_inputs).get_notebook()
        elif component_class.__name__.startswith('SamplePosterior'):
            return SamplePosteriorVbiNotebookGenerator(component_class, component_id, component_inputs, xircuits_filename = xircuits_filename).get_notebook()
        elif component_class.__name__.startswith('SimulationRunner'):
            return TimeSeriesVbiNotebookGenerator(component_class, component_id, component_inputs, xircuits_filename = xircuits_filename).get_notebook()
        return PhasePlaneNotebookGenerator(component_class, component_id, component_inputs, xircuits_id = xircuits_id).get_notebook()

    @staticmethod
    def store(notebook, component_name, xircuits_id):
        file_name = f'{component_name}_widget.ipynb'

        base_dir_web = get_base_dir_web()

        notebook_dir = os.path.join(base_dir_web, NOTEBOOKS_DIR, xircuits_id)
        if not os.path.exists(notebook_dir):
            os.makedirs(notebook_dir, exist_ok=True)

        path = os.path.join(notebook_dir, file_name)

        with open(path, 'w') as f:
            nbformat.write(notebook, f)
            
        LOGGER.info(f'Writing notebook complete at path: {path}')

        base_dir_kernel = get_base_dir_kernel()

        return_path = str(Path(path).relative_to(Path(base_dir_kernel)))

        if IS_WINDOWS:
            windows_expanded_path = return_path.replace("\\", "/")
            LOGGER.info(f'Storing notebook on Windows at path: {windows_expanded_path}')
            return windows_expanded_path

        return return_path


class NotebookGenerator(object):

    def __init__(self, component_class, component_id, component_inputs, xircuits_id=None, xircuits_filename=None):
        self.component_class = component_class
        self.component_id = component_id
        self.component_inputs = component_inputs
        self.xircuits_id = xircuits_id
        self.xircuits_filename = xircuits_filename

        if not os.path.exists(NOTEBOOKS_DIR):
            os.mkdir(NOTEBOOKS_DIR)

        self.notebook = nbformat.v4.new_notebook()

    def get_notebook(self):
        raise NotImplementedError

    def add_code_cell(self, code):
        self._add_cell(nbformat.v4.new_code_cell(code, metadata={'editable': self.edit_cell(), 'deletable': False}))

    def add_markdown_cell(self, text):
        self._add_cell(nbformat.v4.new_markdown_cell(text))

    def _add_cell(self, cell):
        self.notebook['cells'].append(cell)

    def edit_cell(self):
        return False


class TimeSeriesNotebookGenerator(NotebookGenerator):

    def get_notebook(self):
        title = f"""# Interactive viewer for time series"""
        self.add_markdown_cell(title)

        intro = f"#### Run the cell below in order to display the TimeSeriesBrowser widget\n" \
                f"#### It will allow you to browse through the EBRAINS Drive and view the time series from there\n" \
                f"*This widget supports the display of a single time series at a time. If you want to visualize more " \
                f"time series in parallel, please duplicate the cell below to generate new widgets"

        self.add_markdown_cell(intro)
        code = self.time_series_widget()
        self.add_code_cell(code)

        return self.notebook

    def time_series_widget(self):
        code = "%matplotlib widget\n" \
               "\n" \
               "from tvbwidgets.api import TimeSeriesBrowser\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "tsw = TimeSeriesBrowser({0})\n" \
               "display(tsw)"

        inputs_str = self._prepare_component_inputs()
        return code.format(inputs_str)

    def _prepare_component_inputs(self):
        collab_name = self.component_inputs.get('collab_name')
        if collab_name is None:
            return ''

        folder_path = self.component_inputs.get('folder_path')
        return f"'{collab_name}', '{folder_path}'"


class PhasePlaneNotebookGenerator(NotebookGenerator):

    def get_notebook(self):
        title = f"""# Interactive setup for {self.component_class.__name__} model"""
        self.add_markdown_cell(title)

        intro = f"#### Run the cell below in order to display the Phase Plane\n" \
                f"#### Export the model configuration to add it in the Xircuits diagram\n" \
                f"*Some select fields in the Phase Plane are meant to be disabled in this context"
        self.add_markdown_cell(intro)

        inputs_dict = self._prepare_component_inputs()

        export_filename = f"{MODEL_CONFIG_FILE_PREFIX}_{self.component_id}"

        LOGGER.info(f'Exporting path for model: {export_filename}')

        code = PhasePlaneNotebookGenerator.phase_plane(inputs_dict, model=self.component_class().tvb_ht_class,
                                                       export_filename=export_filename)
        self.add_code_cell(code)
        return self.notebook

    @staticmethod
    def phase_plane(inputs_dict, model=Generic2dOscillator, integrator=HeunDeterministic, export_filename=None):
        code = "%matplotlib widget\n" \
               "\n" \
               "import numpy\n" \
               "from tvb.simulator.lab import models, integrators\n" \
               "from tvbwidgets.api import PhasePlaneWidget\n" \
               "from IPython.core.display_functions import display\n" \
               "\n" \
               "w = PhasePlaneWidget(model=models.{0}(**{2}), integrator=integrators.{1}());\n" \
               "w.export_filename = r'{3}' \n" \
               "w.disable_model_dropdown = True \n" \
               "w.disable_export_dropdown = True \n" \
               "display(w.get_widget());"
        return code.format(model.__name__, integrator.__name__, inputs_dict, export_filename)

    def _prepare_component_inputs(self):
        inputs_str = "{"
        param_str = "'{}': {}, "
        for key, val in self.component_inputs.items():
            if type(val) is str:
                if val.startswith('numpy'):
                    inputs_str += param_str.format(key, val)
                elif val in ('True', 'False'):
                    inputs_str += param_str.format(key, f"numpy.array([{bool(val)}])")
                elif val.startswith("'"):
                    inputs_str += param_str.format(key, f"[{val}]")
                elif val.startswith('"'):
                    val = val.replace('"', "'")
                    inputs_str += param_str.format(key, f"[{val}]")
                else:
                    inputs_str += param_str.format(key, f"numpy.array([{val}])")
            else:
                inputs_str += param_str.format(key, f"numpy.array([{val}])")
        return inputs_str + '}'


class SamplePosteriorVbiNotebookGenerator(NotebookGenerator):

    def get_notebook(self):
        title = "# Posterior Pairplot"
        self.add_markdown_cell(title)

        intro = "#### Run the cell below to plot marginals and pairwise marginals of the posterior samples.\n" \
                "Each of the diagonal plots can be interpreted as a 1D-marginal of the distribution that the samples " \
                "were drawn from. Each upper-diagonal plot can be interpreted as a 2D-marginal of the distribution.\n" \
                "\n" \
                "*In case of a remote run, please download the `output_hpc_<xircuits_filename>` folder from the job " \
                "artifacts using tvb-ext-unicore extension and update the paths to `samples.pt` and `theta.pt` " \
                "accordingly."

        self.add_markdown_cell(intro)
        code = self.sample_posterior()
        self.add_code_cell(code)

        return self.notebook

    def sample_posterior(self):
        code = "from sbi.analysis import pairplot\n" \
               "import matplotlib.pyplot as plt\n" \
               "import torch\n" \
               "\n" \
               "limits = [[i, j] for i, j in zip({prior_min}, {prior_max})]\n" \
               "samples = torch.load('{samples_path}', weights_only=True)\n" \
               "theta = torch.load('{theta_path}', weights_only=True)\n" \
               "theta_true = theta[0,:]\n" \
               "fig, ax = pairplot(samples, limits=limits, figsize=(5, 5),\n" \
               "                   points=theta_true, labels={labels},\n"\
               "                   upper='kde', diag='kde',\n"\
               "                   fig_kwargs=dict(\n"\
               "                       points_offdiag=dict(marker='*', markersize=10),\n"\
               "                       points_colors=['g']),\n" \
               "                   diag_kwargs={{'mpl_kwargs': {{'color': 'r'}}}},\n"\
               "                   upper_kwargs={{'mpl_kwargs': {{'cmap': 'Blues'}}}},)\n" \
               "\n" \
               "ax[0,0].tick_params(labelsize=14)\n" \
               "ax[0,0].margins(y=0)\n" \
               "plt.tight_layout()"

        inputs = self._prepare_component_inputs()
        return code.format(**inputs)

    def _prepare_component_inputs(self):
        base_root = os.path.join(get_base_dir_web(), "output")
        output_dir = os.path.join(base_root, "output" + f"_{self.xircuits_filename}")

        # Defaults in case file is missing or in case of a remote run
        prior_min = []
        prior_max = []
        theta_names = []

        priors_path = os.path.join(output_dir, "priors.json")
        try:
            with open(priors_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
            prior_min = data['prior_min']
            prior_max = data['prior_max']
            theta_names = data['theta_names']
        except OSError:
            LOGGER.info(f"Could not load priors from {priors_path}")

        samples = os.path.join(output_dir, "samples.pt").replace("\\", "/") if IS_WINDOWS \
            else os.path.join(output_dir, "samples.pt")

        theta = os.path.join(output_dir, "theta.pt").replace("\\", "/") if IS_WINDOWS \
            else os.path.join(output_dir, "theta.pt")

        return {
            "prior_min": prior_min,
            "prior_max": prior_max,
            "labels": theta_names,
            "samples_path": samples,
            "theta_path": theta,
        }

    def edit_cell(self):
        return True

class TimeSeriesVbiNotebookGenerator(NotebookGenerator):

    def get_notebook(self):
        title = "# Time Series Viewer"
        self.add_markdown_cell(title)

        intro = "#### This notebook helps you visualize the time series produced by a simulation run.\n" \
                "By modifying the code cell below, you can choose which cached simulation output to load and display.\n" \
                "\n" \
                "*In case of a remote run, please download the `output_hpc_<xircuits_filename>` folder from the job " \
                "artifacts using tvb-ext-unicore extension and update the paths to `simulation_data.npz` and " \
                "`model_params.npz` accordingly.\n" \
                "\n"

        self.add_markdown_cell(intro)
        plot_funct = self.vbi_plot_funct()
        self.add_code_cell(plot_funct)
        code = self.plot_timeseries()
        self.add_code_cell(code)
        self.add_code_cell(self.plot_from_batched_simulations())
        self.add_code_cell(self.plot_single_simulation())

        return self.notebook

    @staticmethod
    def vbi_plot_funct():
        code = "from scipy import signal\n" \
               "\n" \
               "# The plotting helper is included inline for now, it will be replaced in the future.\n" \
               "def plot_ts_pxx_jr(data, par, ax, method='welch', **kwargs):\n" \
               "    tspan = data['t']\n" \
               "    y = data['x']\n" \
               "    ax[0].plot(tspan, y.T, label='y1 - y2', **kwargs)\n" \
               "\n" \
               "    if method == 'welch':\n" \
               "        freq, pxx = signal.welch(y, 1000/par['dt'], nperseg=y.shape[1]//2)\n" \
               "    else:\n" \
               "        freq, pxx = fft_signal(y, tspan / 1000)\n" \
               "    ax[1].plot(freq, pxx.T, **kwargs)\n" \
               "    ax[1].set_xlim(0, 50)\n" \
               "    ax[1].set_xlabel('frequency [Hz]')\n" \
               "    ax[0].set_xlabel('time [ms]')\n" \
               "    ax[0].set_ylabel('y1-y2')\n" \
               "    ax[0].margins(x=0)\n" \
               "    plt.tight_layout()\n"

        return code

    def plot_timeseries(self):
        code = "import matplotlib.pyplot as plt\n" \
               "import numpy as np\n" \
               "from xai_components.serialization import *\n" \
               "\n" \
               "data = np.load('{data_path}')\n" \
               "params = load_params_npz('{params_path}')\n"

        inputs = self._prepare_component_inputs()
        return code.format(**inputs)

    @staticmethod
    def plot_from_batched_simulations():
        code = "# Run this cell for CuPy backend: the saved file contains all simulations in one batch.\n" \
               "ts0 = data['x'][:, :, 0].T\n" \
               "data0 = {'t': data['t'], 'x': ts0}\n" \
               "fig, ax = plt.subplots(1, 2, figsize=(10, 3))\n" \
               "plot_ts_pxx_jr(data0, params, ax, alpha=0.6, lw=1)\n" \
               "plt.tight_layout()\n"
        return code

    @staticmethod
    def plot_single_simulation():
        code = "# Run this cell for C++/Numba backend: the saved file contains one simulation only.\n" \
               "fig, ax = plt.subplots(1, 2, figsize=(10, 3))\n" \
               "plot_ts_pxx_jr(data, params, ax, alpha=0.6, lw=1)\n" \
               "plt.tight_layout()\n"
        return code

    def _prepare_component_inputs(self):
        base_root = os.path.join(get_base_dir_web(), "output")
        output_dir = os.path.join(base_root, "output" + f"_{self.xircuits_filename}")

        params_path = os.path.join(output_dir, "model_params.npz").replace("\\", "/") if IS_WINDOWS \
            else os.path.join(output_dir, "model_params.npz")

        data_path = os.path.join(output_dir, "simulation_data.npz").replace("\\", "/") if IS_WINDOWS \
            else os.path.join(output_dir, "simulation_data.npz")
        return {
            "params_path": params_path,
            "data_path": data_path,
        }

    def edit_cell(self):
        return True

def determine_component_class(component_name, component_path):
    component_module = importlib.import_module(component_path.replace('/', '.')[:-3])
    component_class = getattr(component_module, component_name)
    return component_class

import os.path
import shutil
import pytest

from tvbextxircuits import nb_generator
from tvbextxircuits.nb_generator import NotebookGenerator, NotebookFactory
from xai_components.xai_tvb_simulator.simulator import Simulator


TEMP_DIR = "temp_test_dir"
nb_generator.NOTEBOOKS_DIR = TEMP_DIR


def test_notebook_generator():
    notebook_generator = NotebookGenerator(Simulator, '', {})
    assert os.path.exists(nb_generator.NOTEBOOKS_DIR)
    assert notebook_generator.notebook is not None
    assert len(notebook_generator.notebook['cells']) == 0

    notebook_generator.add_code_cell("print('Hello world')")
    assert len(notebook_generator.notebook['cells']) == 1

    notebook_generator.add_markdown_cell("Hello world")
    assert len(notebook_generator.notebook['cells']) == 2

    with pytest.raises(NotImplementedError):
        notebook_generator.get_notebook()


def test_widget_code_generator():
    notebook_factory = NotebookFactory()
    notebook = notebook_factory.get_notebook_for_component('Simulator', 'sim_id',
                                                           'xai_components/xai_tvb_simulator/simulator.py', {},
                                                           'xircuits_id')
    assert notebook is None

    notebook_factory = NotebookFactory()
    notebook = notebook_factory.get_notebook_for_component('ReducedWongWang', 'model_id',
                                                           'xai_components/xai_tvb_models/wong_wang.py', {},
                                                           'xircuits_id')
    assert notebook is not None
    assert "models.ReducedWongWang(**{})" in notebook.cells[2]['source']
    assert f"w.export_filename = r'{os.path.join('temp_test_dir', 'xircuits_id', 'model_model_id')}" in notebook.cells[2]['source']

    assert len(os.listdir(nb_generator.NOTEBOOKS_DIR)) == 0
    notebook_path = notebook_factory.store(notebook, 'model', 'xircuits_id')
    assert os.path.exists(notebook_path)

    notebook_factory = NotebookFactory()
    notebook = notebook_factory.get_notebook_for_component('StoreResultsToDrive', 'store_id',
                                                           'xai_components/xai_storage/store_results.py', {},
                                                           'xircuits_id')
    assert notebook is not None
    assert 'TimeSeriesBrowser()' in notebook.cells[2]['source']

    notebook_factory = NotebookFactory()
    notebook = notebook_factory.get_notebook_for_component('StoreResultsToDrive', 'store_id',
                                                           'xai_components/xai_storage/store_results.py',
                                                           {'collab_name': 'collab', 'folder_path': 'folder'},
                                                           'xircuits_id')
    assert notebook is not None
    assert "TimeSeriesBrowser('collab', 'folder')" in notebook.cells[2]['source']


def teardown_function():
    if os.path.exists(nb_generator.NOTEBOOKS_DIR):
        shutil.rmtree(nb_generator.NOTEBOOKS_DIR)

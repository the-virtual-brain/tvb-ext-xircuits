import json
import os.path
import shutil

from tvbextxircuits import nb_generator
from tvbextxircuits.nb_generator import ModelConfigLoader

SUP_HOPF_DEFAULT_PARAMS = {
    'a': [-0.5],
    'omega': [1],
    'model': 'SupHopf'
}

SUP_HOPF_DEFAULT_PARAMS2 = {
    'a': [0.5],
    'omega': [1],
    'model': 'SupHopf2'
}

TEMP_DIR = "temp_test_dir"


def setup_function():
    os.mkdir(TEMP_DIR)


def test_model_config_loader_false():
    nb_generator.NOTEBOOKS_DIR = TEMP_DIR

    dummy_xircuits_id = "abc-def-ghi-jkl"
    model_config_loader = ModelConfigLoader(dummy_xircuits_id)

    # Test when no xircuits_id folder exists
    result = model_config_loader.load_configs()
    assert result is False

    xircuits_dir = os.path.join(TEMP_DIR, dummy_xircuits_id)
    os.mkdir(xircuits_dir)
    model_config_loader = ModelConfigLoader(dummy_xircuits_id)

    # Test when no model config file exists
    result = model_config_loader.load_configs()
    assert result is False


def create_xircuits_dir():
    dummy_xircuits_id = "abc-def-ghi-jkl"
    xircuits_dir = os.path.join(TEMP_DIR, dummy_xircuits_id)
    os.mkdir(xircuits_dir)
    return xircuits_dir, dummy_xircuits_id


def create_model_config_file(xircuits_dir, model_id=1):
    dummy_model_id = f"abc-def-ghi{model_id}"
    model_config_filename = f"model_{dummy_model_id}.json"
    model_config_file = os.path.join(xircuits_dir, model_config_filename)
    model = SUP_HOPF_DEFAULT_PARAMS
    if model_id == 2:
        model = SUP_HOPF_DEFAULT_PARAMS2
    with open(model_config_file, 'w') as f:
        json.dump({'model': model}, f)
    return dummy_model_id


def test_model_config_loader_single_file():
    xircuits_dir, dummy_xircuits_id = create_xircuits_dir()
    model_config_loader = ModelConfigLoader(dummy_xircuits_id)

    dummy_model_id = create_model_config_file(xircuits_dir)

    result = model_config_loader.load_configs()
    assert type(result) is dict
    assert len(result) == 1
    result_id = list(result.values())[0]['id']
    assert result_id == dummy_model_id
    result_params_a = list(result.values())[0]['params']['a']
    assert result_params_a['name'] == 'a'
    assert result_params_a['value'] == SUP_HOPF_DEFAULT_PARAMS['a'][0]
    assert result_params_a['type'] == 'float'
    assert len(os.listdir(TEMP_DIR)) == 0


def test_model_config_loader_multiple_files():
    xircuits_dir, dummy_xircuits_id = create_xircuits_dir()
    model_config_loader = ModelConfigLoader(dummy_xircuits_id)

    dummy_model_id1 = create_model_config_file(xircuits_dir)
    dummy_model_id2 = create_model_config_file(xircuits_dir, 2)

    result = model_config_loader.load_configs()
    assert type(result) is dict
    assert len(result) == 2
    assert len(os.listdir(TEMP_DIR)) == 0

    def asserts(result_id, dummy_model_id, result_params, default_params):
        assert result_id == dummy_model_id
        assert result_params['a']['name'] == 'a'
        assert result_params['a']['value'] == default_params['a'][0]
        assert result_params['a']['type'] == 'float'

    result_id1 = list(result.values())[0]['id']
    result_params1 = list(result.values())[0]['params']
    result_id2 = list(result.values())[1]['id']
    result_params2 = list(result.values())[1]['params']

    if result_id1 == dummy_model_id1:
        asserts(result_id1, dummy_model_id1, result_params1, SUP_HOPF_DEFAULT_PARAMS)
        asserts(result_id2, dummy_model_id2, result_params2, SUP_HOPF_DEFAULT_PARAMS2)
    else:
        asserts(result_id1, dummy_model_id2, result_params1, SUP_HOPF_DEFAULT_PARAMS2)
        asserts(result_id2, dummy_model_id1, result_params2, SUP_HOPF_DEFAULT_PARAMS)


def teardown_function():
    shutil.rmtree(TEMP_DIR)

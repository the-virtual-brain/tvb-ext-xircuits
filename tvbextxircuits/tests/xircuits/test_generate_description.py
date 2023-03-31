import os
import shutil

import xai_components
import generate_description_files


def test_generate_json(mocker):
    def mock_get_components(self):
        return {'components': [{'package_name': 'xai_components.xai_tvb_models.epileptor', 'class': 'Epileptor'}]}

    mocker.patch('generate_description_files.ComponentsParser.get_components', mock_get_components)

    generate_description_files.main()

    out_path = os.path.join(xai_components.__path__[0], 'xai_tvb_models', 'arguments')
    assert os.path.isdir(out_path)
    assert os.path.exists(os.path.join(out_path, 'epileptor.json'))
    shutil.rmtree(out_path)

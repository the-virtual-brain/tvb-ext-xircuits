# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

from tvb.datatypes.connectivity import Connectivity
from xai_components.base import InArg, OutArg, xai_component
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary
from xai_components.logger.builder import get_logger

LOGGER = get_logger(__name__)


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromFile(TVBComponent):
    """Xircuits component for loading brain connectivity from a file.

    Loads a TVB Connectivity object from a zip file containing structural
    connection data (weights, tract lengths, region centres, and labels).
    If no file path is provided, the default 76-region parcellation from
    tvb_data is used. After loading, a visualization of the connectivity
    weight matrix is displayed.

    Inputs:
        file_path: Path to a connectivity zip file. If not provided,
                   defaults to 'connectivity_76.zip' from tvb_data.

    Output:
        connectivity: Configured TVB Connectivity object containing
                      weights, tract lengths, and region information.
    """
    file_path: InArg[str]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.file_path = InArg(None)
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        from matplotlib import pyplot as plt

        file_path = self.file_path.value
        if not file_path:
            file_path = 'connectivity_76.zip'  # default from tvb_data

        try:
            connectivity = Connectivity.from_file(file_path)
        except Exception as e:
            LOGGER.error(f"Failed to load connectivity from '{file_path}': {e}")
            raise ValueError(
                f"Could not load connectivity file '{file_path}'. "
                f"Please check that the file exists and is a valid "
                f"TVB connectivity zip file."
            ) from e

        connectivity.configure()

        self.connectivity.value = connectivity
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.title('Connectivity Weights')
        try:
            plt.show(block=False)
        except Exception:
            LOGGER.warning("Could not display plot in current environment.")

# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.connectivity import Connectivity
from xai_components.base import InArg, OutArg, xai_component
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromFile(TVBComponent):
    file_path: InArg[str]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.file_path = InArg(None)
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt
        from tvb.datatypes.connectivity import Connectivity

        file_path = self.file_path.value
        if not file_path:
            file_path = 'connectivity_76.zip'  # default from tvb_data
        connectivity = Connectivity.from_file(file_path)
        connectivity.configure()

        self.connectivity.value = connectivity
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.show()

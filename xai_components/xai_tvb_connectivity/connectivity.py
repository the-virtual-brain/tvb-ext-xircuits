# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.connectivity import Connectivity

from xai_components.base import InArg, OutArg, Component, xai_component
from xai_components.utils import print_component_summary


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromFile(Component):
    file_name: InArg[str]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.file_name = InArg('connectivity_76.zip')
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt
        from tvb.simulator.lab import connectivity

        self.connectivity.value = connectivity.Connectivity.from_file(self.file_name.value)
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.show()
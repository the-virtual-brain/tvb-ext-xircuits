# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.adapters.creators import siibra_base as sb
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


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromSiibra(Component):
    atlas: InArg[str]
    parcellation: InArg[str]
    subject_id: InArg[str]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.atlas = InArg(sb.DEFAULT_ATLAS)
        self.parcellation = InArg(sb.DEFAULT_PARCELLATION)
        self.subject_id = InArg('000')
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt

        atlas = self.atlas.value
        parcellation = self.parcellation.value
        subject_id = self.subject_id.value

        sc_dict, _ = sb.get_connectivities_from_kg(atlas=atlas, parcellation=parcellation,
                                                   subject_ids=subject_id,
                                                   compute_fc=False)

        self.connectivity.value = sc_dict[subject_id]
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.show()

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


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromSiibra(Component):
    conn_from_siibra: InArg[dict]
    subject_id: InArg[str]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.conn_from_siibra = InArg(None)
        self.subject_id = InArg(None)
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt

        conn_dict = self.conn_from_siibra.value
        all_subjects = list(conn_dict.keys())   # list of all the subjects for which there's a connectivity
        subject_id = self.subject_id.value
        if not subject_id:
            subject_id = all_subjects[0]    # if no subject id was provided, get the first connectivity
        elif subject_id not in all_subjects:
            raise ValueError(f'There is no connectivity for subject \'{subject_id}\' among the connectivities '
                             f'that were provided')

        self.connectivity.value = conn_dict[subject_id]
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.show()

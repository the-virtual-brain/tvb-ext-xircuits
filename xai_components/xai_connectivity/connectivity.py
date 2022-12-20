# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import os
from siibra.retrieval import SiibraHttpRequestError
from tvb.adapters.creators import siibra_base as sb
from tvb.datatypes.connectivity import Connectivity
from tvbwidgets.core.auth import get_current_token
from xai_components.base import InArg, OutArg, Component, xai_component
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

        token = get_current_token()
        os.environ['HBP_AUTH_TOKEN'] = token

        try:
            sc_dict, _ = sb.get_connectivities_from_kg(atlas=atlas, parcellation=parcellation,
                                                       subject_ids=subject_id,
                                                       compute_fc=False)
            connectivity = sc_dict[subject_id]
            connectivity.configure()

            self.connectivity.value = connectivity
            print_component_summary(self.connectivity.value)

            plt.imshow(self.connectivity.value.weights, interpolation='none')
            plt.show()
        except SiibraHttpRequestError as e:
            if e.response.status_code in [401, 403]:
                raise ConnectionError('Invalid EBRAINS authentication token. Please provide a new one as environment '
                                      'variable HBP_AUTH_TOKEN.')
            else:
                raise ConnectionError('We could not complete the operation. '
                                      'Please check the logs and contact the development team from TVB, siibra or EBRAINS KG.')

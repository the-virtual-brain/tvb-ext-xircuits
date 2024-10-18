# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from typing import Literal
from siibra.retrieval import SiibraHttpRequestError
from tvb.adapters.creators import siibra_base as sb
from tvb.datatypes.connectivity import Connectivity
from xai_components.base import InArg, OutArg, Component, xai_component
from xai_components.utils import print_component_summary


@xai_component(color='rgb(85, 37, 130)')
class ConnectivityFromSiibra(Component):
    atlas: InArg[Literal['Multilevel Human Atlas']]
    parcellation: InArg[Literal['Julich-Brain Cytoarchitectonic Atlas (v3.0.3)', 'Julich-Brain Cytoarchitectonic Atlas (v2.9)']]
    subject_id: InArg[str]
    cohort: InArg[Literal['HCP', '1000BRAINS']]

    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False
        self.atlas = InArg(sb.HUMAN_ATLAS)
        self.parcellation = InArg(sb.JULICH_3_0_3)
        self.cohort = InArg(sb.HCP_COHORT)
        self.subject_id = InArg('000')
        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt

        atlas = self.atlas.value
        parcellation = self.parcellation.value
        cohort = self.cohort.value
        subject_id = self.subject_id.value

        try:
            sc_dict, _ = sb.get_connectivities_from_kg(atlas=atlas, parcellation=parcellation, cohort=cohort,
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

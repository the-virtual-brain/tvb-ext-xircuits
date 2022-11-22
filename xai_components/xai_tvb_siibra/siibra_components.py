# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from tvb.adapters.creators import siibra_base as sb
from xai_components.base import Component, xai_component, InArg, OutArg


@xai_component(color='rgb(217, 141, 100)')
class SiibraCreator(Component):
    atlas: InArg[str]
    parcellation: InArg[str]
    subject_ids: InArg[str]
    compute_functional_connectivity: InArg[bool]

    connectivities_dict: OutArg[dict]
    functional_connectivities: OutArg[dict]

    def __init__(self):
        self.done = False
        self.atlas = InArg(sb.DEFAULT_ATLAS)
        self.parcellation = InArg(sb.DEFAULT_PARCELLATION)
        self.subject_ids = InArg('000')
        self.compute_functional_connectivity = InArg(False)
        self.connectivities_dict = OutArg({})
        self.functional_connectivities = OutArg({})

    def execute(self, ctx) -> None:

        atlas = self.atlas.value
        parcellation = self.parcellation.value
        subject_ids = self.subject_ids.value
        compute_fc = self.compute_functional_connectivity.value

        sc_dict, fc_dict = sb.get_connectivities_from_kg(atlas=atlas, parcellation=parcellation, subject_ids=subject_ids,
                                                         compute_fc=compute_fc)
        self.connectivities_dict.value = sc_dict
        self.functional_connectivities.value = fc_dict
        print(self.connectivities_dict.value)

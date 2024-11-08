# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2024, TVB Widgets Team
#
from tvb.datatypes.connectivity import Connectivity
from tvb.datatypes.region_mapping import RegionMapping
from tvb.datatypes.surfaces import Surface

from xai_components.base import InArg, OutArg, xai_component, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import set_defaults, set_values, print_component_summary


@xai_component(color='rgb(120, 70, 31)')
class RegionMapping(TVBComponent):
    file_path: InArg[str]
    connectivity: InCompArg[Connectivity]
    surface: InCompArg[Surface]

    region_mapping: OutArg[RegionMapping]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.region_mapping import RegionMapping
        return RegionMapping

    def __init__(self):
        self.done = False
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)
        self.region_mapping = OutArg(None)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'regionMapping_16k_76.txt'  # default from tvb_data
        region_mapping = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, region_mapping)

        self.region_mapping.value = region_mapping
        print_component_summary(self.region_mapping.value)

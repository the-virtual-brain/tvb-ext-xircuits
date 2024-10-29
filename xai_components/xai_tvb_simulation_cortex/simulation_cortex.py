# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2024, TVB Widgets Team
#
from tvb.datatypes.cortex import Cortex
from tvb.datatypes.region_mapping import RegionMapping
from xai_components.base import xai_component, InArg, OutArg, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import set_values, print_component_summary, set_defaults


@xai_component(color='rgb(0, 116, 92)')
class SimulationCortex(TVBComponent):
    region_mapping_data: InCompArg[RegionMapping]
    coupling_strength: InArg[list]

    simulation_cortex: OutArg[Cortex]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.cortex import Cortex
        return Cortex

    def __init__(self):
        self.region_mapping_data = InCompArg(None)
        self.coupling_strength = InArg(None)
        self.simulation_cortex = OutArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        simulation_cortex = self.tvb_ht_class()
        set_values(self, simulation_cortex)
        simulation_cortex.configure()

        self.simulation_cortex.value = simulation_cortex
        print_component_summary(self.simulation_cortex.value)



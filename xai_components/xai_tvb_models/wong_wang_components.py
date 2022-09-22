# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(101, 179, 46)')
class ReducedWongWang(Component):
    from tvb.simulator.models.wong_wang import ReducedWongWang
    a: InArg[list]
    b: InArg[list]
    d: InArg[list]
    gamma: InArg[list]
    tau_s: InArg[list]
    w: InArg[list]
    J_N: InArg[list]
    I_o: InArg[list]
    sigma_noise: InArg[list]
    variables_of_interest: InArg[list]

    reducedWongWang: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ReducedWongWang)

    def execute(self, ctx) -> None:
        reducedWongWang = self.ReducedWongWang()

        set_values(self, reducedWongWang)
        self.reducedWongWang.value = reducedWongWang
        print_component_summary(self.reducedWongWang.value)
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
    a: InArg[float]
    b: InArg[float]
    d: InArg[float]
    gamma: InArg[float]
    tau_s: InArg[float]
    w: InArg[float]
    J_N: InArg[float]
    I_o: InArg[float]
    sigma_noise: InArg[float]
    variables_of_interest: InArg[list]

    reducedWongWang: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ReducedWongWang)

    def execute(self, ctx) -> None:
        reducedWongWang = self.ReducedWongWang()

        set_values(self, reducedWongWang)
        self.reducedWongWang.value = reducedWongWang
        print_component_summary(self.reducedWongWang.value)
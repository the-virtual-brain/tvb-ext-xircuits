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
class ReducedWongWangExcInh(Component):
    from tvb.simulator.models.wong_wang_exc_inh import ReducedWongWangExcInh
    a_e: InArg[list]
    b_e: InArg[list]
    d_e: InArg[list]
    gamma_e: InArg[list]
    tau_e: InArg[list]
    w_p: InArg[list]
    J_N: InArg[list]
    W_e: InArg[list]
    a_i: InArg[list]
    b_i: InArg[list]
    d_i: InArg[list]
    gamma_i: InArg[list]
    tau_i: InArg[list]
    J_i: InArg[list]
    W_i: InArg[list]
    I_o: InArg[list]
    I_ext: InArg[list]
    G: InArg[list]
    lamda: InArg[list]
    variables_of_interest: InArg[list]

    reducedWongWangExcInh: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ReducedWongWangExcInh)

    def execute(self, ctx) -> None:
        reducedWongWangExcInh = self.ReducedWongWangExcInh()

        set_values(self, reducedWongWangExcInh)
        self.reducedWongWangExcInh.value = reducedWongWangExcInh
        print_component_summary(self.reducedWongWangExcInh.value)


@xai_component(color='rgb(101, 179, 46)')
class DecoBalancedExcInh(Component):
    from tvb.simulator.models.wong_wang_exc_inh import DecoBalancedExcInh
    M_i: InArg[list]

    decoBalancedExcInh: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.DecoBalancedExcInh)

    def execute(self, ctx) -> None:
        decoBalancedExcInh = self.DecoBalancedExcInh()

        set_values(self, decoBalancedExcInh)
        self.decoBalancedExcInh.value = decoBalancedExcInh
        print_component_summary(self.decoBalancedExcInh.value)


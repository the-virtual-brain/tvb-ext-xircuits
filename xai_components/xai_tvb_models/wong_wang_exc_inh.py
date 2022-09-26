# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class ReducedWongWangExcInh(ComponentWithWidget):
    a_e: InArg[float]
    b_e: InArg[float]
    d_e: InArg[float]
    gamma_e: InArg[float]
    tau_e: InArg[float]
    w_p: InArg[float]
    J_N: InArg[float]
    W_e: InArg[float]
    a_i: InArg[float]
    b_i: InArg[float]
    d_i: InArg[float]
    gamma_i: InArg[float]
    tau_i: InArg[float]
    J_i: InArg[float]
    W_i: InArg[float]
    I_o: InArg[float]
    I_ext: InArg[float]
    G: InArg[float]
    lamda: InArg[float]
    variables_of_interest: InArg[list]

    reducedWongWangExcInh: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.wong_wang_exc_inh import ReducedWongWangExcInh
        return ReducedWongWangExcInh

    def execute(self, ctx) -> None:
        reducedWongWangExcInh = self.tvb_ht_class()

        set_values(self, reducedWongWangExcInh)
        self.reducedWongWangExcInh.value = reducedWongWangExcInh
        print_component_summary(self.reducedWongWangExcInh.value)


@xai_component(color='rgb(101, 179, 46)')
class DecoBalancedExcInh(ComponentWithWidget):
    M_i: InArg[float]
    a_e: InArg[float]
    b_e: InArg[float]
    d_e: InArg[float]
    gamma_e: InArg[float]
    tau_e: InArg[float]
    w_p: InArg[float]
    J_N: InArg[float]
    W_e: InArg[float]
    a_i: InArg[float]
    b_i: InArg[float]
    d_i: InArg[float]
    gamma_i: InArg[float]
    tau_i: InArg[float]
    J_i: InArg[float]
    W_i: InArg[float]
    I_o: InArg[float]
    I_ext: InArg[float]
    G: InArg[float]
    lamda: InArg[float]
    variables_of_interest: InArg[list]

    decoBalancedExcInh: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.wong_wang_exc_inh import DecoBalancedExcInh
        return DecoBalancedExcInh

    def execute(self, ctx) -> None:
        decoBalancedExcInh = self.tvb_ht_class()

        set_values(self, decoBalancedExcInh)
        self.decoBalancedExcInh.value = decoBalancedExcInh
        print_component_summary(self.decoBalancedExcInh.value)

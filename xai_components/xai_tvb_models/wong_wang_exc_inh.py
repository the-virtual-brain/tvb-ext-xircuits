# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy
from tvb.simulator.models.base import Model
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class ReducedWongWangExcInh(ComponentWithWidget):
    a_e: InArg[Union[float, numpy.ndarray]]
    b_e: InArg[Union[float, numpy.ndarray]]
    d_e: InArg[Union[float, numpy.ndarray]]
    gamma_e: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    w_p: InArg[Union[float, numpy.ndarray]]
    J_N: InArg[Union[float, numpy.ndarray]]
    W_e: InArg[Union[float, numpy.ndarray]]
    a_i: InArg[Union[float, numpy.ndarray]]
    b_i: InArg[Union[float, numpy.ndarray]]
    d_i: InArg[Union[float, numpy.ndarray]]
    gamma_i: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    J_i: InArg[Union[float, numpy.ndarray]]
    W_i: InArg[Union[float, numpy.ndarray]]
    I_o: InArg[Union[float, numpy.ndarray]]
    I_ext: InArg[Union[float, numpy.ndarray]]
    G: InArg[Union[float, numpy.ndarray]]
    lamda: InArg[Union[float, numpy.ndarray]]
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
    M_i: InArg[Union[float, numpy.ndarray]]
    a_e: InArg[Union[float, numpy.ndarray]]
    b_e: InArg[Union[float, numpy.ndarray]]
    d_e: InArg[Union[float, numpy.ndarray]]
    gamma_e: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    w_p: InArg[Union[float, numpy.ndarray]]
    J_N: InArg[Union[float, numpy.ndarray]]
    W_e: InArg[Union[float, numpy.ndarray]]
    a_i: InArg[Union[float, numpy.ndarray]]
    b_i: InArg[Union[float, numpy.ndarray]]
    d_i: InArg[Union[float, numpy.ndarray]]
    gamma_i: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    J_i: InArg[Union[float, numpy.ndarray]]
    W_i: InArg[Union[float, numpy.ndarray]]
    I_o: InArg[Union[float, numpy.ndarray]]
    I_ext: InArg[Union[float, numpy.ndarray]]
    G: InArg[Union[float, numpy.ndarray]]
    lamda: InArg[Union[float, numpy.ndarray]]
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

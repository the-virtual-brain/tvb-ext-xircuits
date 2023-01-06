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
class ZerlautAdaptationFirstOrder(ComponentWithWidget):
    g_L: InArg[Union[float, numpy.ndarray]]
    E_L_e: InArg[Union[float, numpy.ndarray]]
    E_L_i: InArg[Union[float, numpy.ndarray]]
    C_m: InArg[Union[float, numpy.ndarray]]
    b_e: InArg[Union[float, numpy.ndarray]]
    a_e: InArg[Union[float, numpy.ndarray]]
    b_i: InArg[Union[float, numpy.ndarray]]
    a_i: InArg[Union[float, numpy.ndarray]]
    tau_w_e: InArg[Union[float, numpy.ndarray]]
    tau_w_i: InArg[Union[float, numpy.ndarray]]
    E_e: InArg[Union[float, numpy.ndarray]]
    E_i: InArg[Union[float, numpy.ndarray]]
    Q_e: InArg[Union[float, numpy.ndarray]]
    Q_i: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    N_tot: InArg[Union[int, numpy.ndarray]]
    p_connect: InArg[Union[float, numpy.ndarray]]
    g: InArg[Union[float, numpy.ndarray]]
    K_ext_e: InArg[Union[int, numpy.ndarray]]
    K_ext_i: InArg[Union[int, numpy.ndarray]]
    T: InArg[Union[float, numpy.ndarray]]
    P_e: InArg[Union[float, numpy.ndarray]]
    P_i: InArg[Union[float, numpy.ndarray]]
    external_input_ex_ex: InArg[Union[float, numpy.ndarray]]
    external_input_ex_in: InArg[Union[float, numpy.ndarray]]
    external_input_in_ex: InArg[Union[float, numpy.ndarray]]
    external_input_in_in: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    zerlautAdaptationFirstOrder: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.zerlaut import ZerlautAdaptationFirstOrder
        return ZerlautAdaptationFirstOrder

    def execute(self, ctx) -> None:
        zerlautAdaptationFirstOrder = self.tvb_ht_class()

        set_values(self, zerlautAdaptationFirstOrder)
        self.zerlautAdaptationFirstOrder.value = zerlautAdaptationFirstOrder
        print_component_summary(self.zerlautAdaptationFirstOrder.value)


@xai_component(color='rgb(101, 179, 46)')
class ZerlautAdaptationSecondOrder(ComponentWithWidget):
    g_L: InArg[Union[float, numpy.ndarray]]
    E_L_e: InArg[Union[float, numpy.ndarray]]
    E_L_i: InArg[Union[float, numpy.ndarray]]
    C_m: InArg[Union[float, numpy.ndarray]]
    b_e: InArg[Union[float, numpy.ndarray]]
    a_e: InArg[Union[float, numpy.ndarray]]
    b_i: InArg[Union[float, numpy.ndarray]]
    a_i: InArg[Union[float, numpy.ndarray]]
    tau_w_e: InArg[Union[float, numpy.ndarray]]
    tau_w_i: InArg[Union[float, numpy.ndarray]]
    E_e: InArg[Union[float, numpy.ndarray]]
    E_i: InArg[Union[float, numpy.ndarray]]
    Q_e: InArg[Union[float, numpy.ndarray]]
    Q_i: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    N_tot: InArg[Union[int, numpy.ndarray]]
    p_connect: InArg[Union[float, numpy.ndarray]]
    g: InArg[Union[float, numpy.ndarray]]
    K_ext_e: InArg[Union[int, numpy.ndarray]]
    K_ext_i: InArg[Union[int, numpy.ndarray]]
    T: InArg[Union[float, numpy.ndarray]]
    P_e: InArg[Union[float, numpy.ndarray]]
    P_i: InArg[Union[float, numpy.ndarray]]
    external_input_ex_ex: InArg[Union[float, numpy.ndarray]]
    external_input_ex_in: InArg[Union[float, numpy.ndarray]]
    external_input_in_ex: InArg[Union[float, numpy.ndarray]]
    external_input_in_in: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    zerlautAdaptationSecondOrder: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.zerlaut import ZerlautAdaptationSecondOrder
        return ZerlautAdaptationSecondOrder

    def execute(self, ctx) -> None:
        zerlautAdaptationSecondOrder = self.tvb_ht_class()

        set_values(self, zerlautAdaptationSecondOrder)
        self.zerlautAdaptationSecondOrder.value = zerlautAdaptationSecondOrder
        print_component_summary(self.zerlautAdaptationSecondOrder.value)

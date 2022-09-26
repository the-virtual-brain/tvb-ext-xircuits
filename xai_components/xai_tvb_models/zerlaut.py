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
class ZerlautAdaptationFirstOrder(ComponentWithWidget):
    g_L: InArg[float]
    E_L_e: InArg[float]
    E_L_i: InArg[float]
    C_m: InArg[float]
    b_e: InArg[float]
    a_e: InArg[float]
    b_i: InArg[float]
    a_i: InArg[float]
    tau_w_e: InArg[float]
    tau_w_i: InArg[float]
    E_e: InArg[float]
    E_i: InArg[float]
    Q_e: InArg[float]
    Q_i: InArg[float]
    tau_e: InArg[float]
    tau_i: InArg[float]
    N_tot: InArg[int]
    p_connect: InArg[float]
    g: InArg[float]
    K_ext_e: InArg[int]
    K_ext_i: InArg[int]
    T: InArg[float]
    P_e: InArg[float]
    P_i: InArg[float]
    external_input_ex_ex: InArg[float]
    external_input_ex_in: InArg[float]
    external_input_in_ex: InArg[float]
    external_input_in_in: InArg[float]
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
    g_L: InArg[float]
    E_L_e: InArg[float]
    E_L_i: InArg[float]
    C_m: InArg[float]
    b_e: InArg[float]
    a_e: InArg[float]
    b_i: InArg[float]
    a_i: InArg[float]
    tau_w_e: InArg[float]
    tau_w_i: InArg[float]
    E_e: InArg[float]
    E_i: InArg[float]
    Q_e: InArg[float]
    Q_i: InArg[float]
    tau_e: InArg[float]
    tau_i: InArg[float]
    N_tot: InArg[int]
    p_connect: InArg[float]
    g: InArg[float]
    K_ext_e: InArg[int]
    K_ext_i: InArg[int]
    T: InArg[float]
    P_e: InArg[float]
    P_i: InArg[float]
    external_input_ex_ex: InArg[float]
    external_input_ex_in: InArg[float]
    external_input_in_ex: InArg[float]
    external_input_in_in: InArg[float]
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

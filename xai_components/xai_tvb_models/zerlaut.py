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
class ZerlautAdaptationFirstOrder(Component):
    from tvb.simulator.models.zerlaut import ZerlautAdaptationFirstOrder
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

    def __init__(self):
        set_defaults(self, self.ZerlautAdaptationFirstOrder)

    def execute(self, ctx) -> None:
        zerlautAdaptationFirstOrder = self.ZerlautAdaptationFirstOrder()

        set_values(self, zerlautAdaptationFirstOrder)
        self.zerlautAdaptationFirstOrder.value = zerlautAdaptationFirstOrder
        print_component_summary(self.zerlautAdaptationFirstOrder.value)


@xai_component(color='rgb(101, 179, 46)')
class ZerlautAdaptationSecondOrder(Component):
    from tvb.simulator.models.zerlaut import ZerlautAdaptationSecondOrder
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

    def __init__(self):
        set_defaults(self, self.ZerlautAdaptationSecondOrder)

    def execute(self, ctx) -> None:
        zerlautAdaptationSecondOrder = self.ZerlautAdaptationSecondOrder()

        set_values(self, zerlautAdaptationSecondOrder)
        self.zerlautAdaptationSecondOrder.value = zerlautAdaptationSecondOrder
        print_component_summary(self.zerlautAdaptationSecondOrder.value)


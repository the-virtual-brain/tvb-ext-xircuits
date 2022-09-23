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
    g_L: InArg[list]
    E_L_e: InArg[list]
    E_L_i: InArg[list]
    C_m: InArg[list]
    b_e: InArg[list]
    a_e: InArg[list]
    b_i: InArg[list]
    a_i: InArg[list]
    tau_w_e: InArg[list]
    tau_w_i: InArg[list]
    E_e: InArg[list]
    E_i: InArg[list]
    Q_e: InArg[list]
    Q_i: InArg[list]
    tau_e: InArg[list]
    tau_i: InArg[list]
    N_tot: InArg[list]
    p_connect: InArg[list]
    g: InArg[list]
    K_ext_e: InArg[list]
    K_ext_i: InArg[list]
    T: InArg[list]
    P_e: InArg[list]
    P_i: InArg[list]
    external_input_ex_ex: InArg[list]
    external_input_ex_in: InArg[list]
    external_input_in_ex: InArg[list]
    external_input_in_in: InArg[list]
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
    variables_of_interest: InArg[list]

    zerlautAdaptationSecondOrder: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ZerlautAdaptationSecondOrder)

    def execute(self, ctx) -> None:
        zerlautAdaptationSecondOrder = self.ZerlautAdaptationSecondOrder()

        set_values(self, zerlautAdaptationSecondOrder)
        self.zerlautAdaptationSecondOrder.value = zerlautAdaptationSecondOrder
        print_component_summary(self.zerlautAdaptationSecondOrder.value)


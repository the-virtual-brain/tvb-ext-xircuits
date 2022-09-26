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
class WilsonCowan(Component):
    from tvb.simulator.models.wilson_cowan import WilsonCowan
    c_ee: InArg[float]
    c_ei: InArg[float]
    c_ie: InArg[float]
    c_ii: InArg[float]
    tau_e: InArg[float]
    tau_i: InArg[float]
    a_e: InArg[float]
    b_e: InArg[float]
    c_e: InArg[float]
    theta_e: InArg[float]
    a_i: InArg[float]
    b_i: InArg[float]
    theta_i: InArg[float]
    c_i: InArg[float]
    r_e: InArg[float]
    r_i: InArg[float]
    k_e: InArg[float]
    k_i: InArg[float]
    P: InArg[float]
    Q: InArg[float]
    alpha_e: InArg[float]
    alpha_i: InArg[float]
    shift_sigmoid: InArg[bool]
    variables_of_interest: InArg[list]

    wilsonCowan: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.WilsonCowan)

    def execute(self, ctx) -> None:
        wilsonCowan = self.WilsonCowan()

        set_values(self, wilsonCowan)
        self.wilsonCowan.value = wilsonCowan
        print_component_summary(self.wilsonCowan.value)
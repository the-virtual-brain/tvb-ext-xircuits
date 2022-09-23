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
    c_ee: InArg[list]
    c_ei: InArg[list]
    c_ie: InArg[list]
    c_ii: InArg[list]
    tau_e: InArg[list]
    tau_i: InArg[list]
    a_e: InArg[list]
    b_e: InArg[list]
    c_e: InArg[list]
    theta_e: InArg[list]
    a_i: InArg[list]
    b_i: InArg[list]
    theta_i: InArg[list]
    c_i: InArg[list]
    r_e: InArg[list]
    r_i: InArg[list]
    k_e: InArg[list]
    k_i: InArg[list]
    P: InArg[list]
    Q: InArg[list]
    alpha_e: InArg[list]
    alpha_i: InArg[list]
    shift_sigmoid: InArg[list]
    variables_of_interest: InArg[list]

    wilsonCowan: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.WilsonCowan)

    def execute(self, ctx) -> None:
        wilsonCowan = self.WilsonCowan()

        set_values(self, wilsonCowan)
        self.wilsonCowan.value = wilsonCowan
        print_component_summary(self.wilsonCowan.value)
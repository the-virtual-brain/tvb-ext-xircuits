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
class WilsonCowan(ComponentWithWidget):
    c_ee: InArg[Union[float, numpy.ndarray]]
    c_ei: InArg[Union[float, numpy.ndarray]]
    c_ie: InArg[Union[float, numpy.ndarray]]
    c_ii: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    a_e: InArg[Union[float, numpy.ndarray]]
    b_e: InArg[Union[float, numpy.ndarray]]
    c_e: InArg[Union[float, numpy.ndarray]]
    theta_e: InArg[Union[float, numpy.ndarray]]
    a_i: InArg[Union[float, numpy.ndarray]]
    b_i: InArg[Union[float, numpy.ndarray]]
    theta_i: InArg[Union[float, numpy.ndarray]]
    c_i: InArg[Union[float, numpy.ndarray]]
    r_e: InArg[Union[float, numpy.ndarray]]
    r_i: InArg[Union[float, numpy.ndarray]]
    k_e: InArg[Union[float, numpy.ndarray]]
    k_i: InArg[Union[float, numpy.ndarray]]
    P: InArg[Union[float, numpy.ndarray]]
    Q: InArg[Union[float, numpy.ndarray]]
    alpha_e: InArg[Union[float, numpy.ndarray]]
    alpha_i: InArg[Union[float, numpy.ndarray]]
    shift_sigmoid: InArg[Union[bool, numpy.ndarray]]
    variables_of_interest: InArg[list]

    wilsonCowan: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.wilson_cowan import WilsonCowan
        return WilsonCowan

    def execute(self, ctx) -> None:
        wilsonCowan = self.tvb_ht_class()

        set_values(self, wilsonCowan)
        self.wilsonCowan.value = wilsonCowan
        print_component_summary(self.wilsonCowan.value)

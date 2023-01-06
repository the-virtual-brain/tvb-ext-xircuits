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
class ReducedWongWang(ComponentWithWidget):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    gamma: InArg[Union[float, numpy.ndarray]]
    tau_s: InArg[Union[float, numpy.ndarray]]
    w: InArg[Union[float, numpy.ndarray]]
    J_N: InArg[Union[float, numpy.ndarray]]
    I_o: InArg[Union[float, numpy.ndarray]]
    sigma_noise: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    reducedWongWang: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.wong_wang import ReducedWongWang
        return ReducedWongWang

    def execute(self, ctx) -> None:
        reducedWongWang = self.tvb_ht_class()

        set_values(self, reducedWongWang)
        self.reducedWongWang.value = reducedWongWang
        print_component_summary(self.reducedWongWang.value)

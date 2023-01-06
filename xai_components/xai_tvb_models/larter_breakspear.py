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
class LarterBreakspear(ComponentWithWidget):
    gCa: InArg[Union[float, numpy.ndarray]]
    gK: InArg[Union[float, numpy.ndarray]]
    gL: InArg[Union[float, numpy.ndarray]]
    phi: InArg[Union[float, numpy.ndarray]]
    gNa: InArg[Union[float, numpy.ndarray]]
    TK: InArg[Union[float, numpy.ndarray]]
    TCa: InArg[Union[float, numpy.ndarray]]
    TNa: InArg[Union[float, numpy.ndarray]]
    VCa: InArg[Union[float, numpy.ndarray]]
    VK: InArg[Union[float, numpy.ndarray]]
    VL: InArg[Union[float, numpy.ndarray]]
    VNa: InArg[Union[float, numpy.ndarray]]
    d_K: InArg[Union[float, numpy.ndarray]]
    tau_K: InArg[Union[float, numpy.ndarray]]
    d_Na: InArg[Union[float, numpy.ndarray]]
    d_Ca: InArg[Union[float, numpy.ndarray]]
    aei: InArg[Union[float, numpy.ndarray]]
    aie: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    C: InArg[Union[float, numpy.ndarray]]
    ane: InArg[Union[float, numpy.ndarray]]
    ani: InArg[Union[float, numpy.ndarray]]
    aee: InArg[Union[float, numpy.ndarray]]
    Iext: InArg[Union[float, numpy.ndarray]]
    rNMDA: InArg[Union[float, numpy.ndarray]]
    VT: InArg[Union[float, numpy.ndarray]]
    d_V: InArg[Union[float, numpy.ndarray]]
    ZT: InArg[Union[float, numpy.ndarray]]
    d_Z: InArg[Union[float, numpy.ndarray]]
    QV_max: InArg[Union[float, numpy.ndarray]]
    QZ_max: InArg[Union[float, numpy.ndarray]]
    t_scale: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    larterBreakspear: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.larter_breakspear import LarterBreakspear
        return LarterBreakspear

    def execute(self, ctx) -> None:
        larterBreakspear = self.tvb_ht_class()

        set_values(self, larterBreakspear)
        self.larterBreakspear.value = larterBreakspear
        print_component_summary(self.larterBreakspear.value)

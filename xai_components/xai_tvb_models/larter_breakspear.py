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
class LarterBreakspear(ComponentWithWidget):
    gCa: InArg[float]
    gK: InArg[float]
    gL: InArg[float]
    phi: InArg[float]
    gNa: InArg[float]
    TK: InArg[float]
    TCa: InArg[float]
    TNa: InArg[float]
    VCa: InArg[float]
    VK: InArg[float]
    VL: InArg[float]
    VNa: InArg[float]
    d_K: InArg[float]
    tau_K: InArg[float]
    d_Na: InArg[float]
    d_Ca: InArg[float]
    aei: InArg[float]
    aie: InArg[float]
    b: InArg[float]
    C: InArg[float]
    ane: InArg[float]
    ani: InArg[float]
    aee: InArg[float]
    Iext: InArg[float]
    rNMDA: InArg[float]
    VT: InArg[float]
    d_V: InArg[float]
    ZT: InArg[float]
    d_Z: InArg[float]
    QV_max: InArg[float]
    QZ_max: InArg[float]
    t_scale: InArg[float]
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

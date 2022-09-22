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
class LarterBreakspear(Component):
    from tvb.simulator.models.larter_breakspear import LarterBreakspear
    gCa: InArg[list]
    gK: InArg[list]
    gL: InArg[list]
    phi: InArg[list]
    gNa: InArg[list]
    TK: InArg[list]
    TCa: InArg[list]
    TNa: InArg[list]
    VCa: InArg[list]
    VK: InArg[list]
    VL: InArg[list]
    VNa: InArg[list]
    d_K: InArg[list]
    tau_K: InArg[list]
    d_Na: InArg[list]
    d_Ca: InArg[list]
    aei: InArg[list]
    aie: InArg[list]
    b: InArg[list]
    C: InArg[list]
    ane: InArg[list]
    ani: InArg[list]
    aee: InArg[list]
    Iext: InArg[list]
    rNMDA: InArg[list]
    VT: InArg[list]
    d_V: InArg[list]
    ZT: InArg[list]
    d_Z: InArg[list]
    QV_max: InArg[list]
    QZ_max: InArg[list]
    t_scale: InArg[list]
    variables_of_interest: InArg[list]

    larterbreakspear: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.LarterBreakspear)

    def execute(self, ctx) -> None:
        larterbreakspear = self.LarterBreakspear()

        set_values(self, larterbreakspear)
        self.larterbreakspear.value = larterbreakspear
        print_component_summary(self.larterbreakspear.value)
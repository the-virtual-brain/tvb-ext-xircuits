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
class EpileptorCodim3(Component):
    from tvb.simulator.models.epileptorcodim3 import EpileptorCodim3
    mu1_start: InArg[float]
    mu2_start: InArg[float]
    nu_start: InArg[float]
    mu1_stop: InArg[float]
    mu2_stop: InArg[float]
    nu_stop: InArg[float]
    b: InArg[float]
    R: InArg[float]
    c: InArg[float]
    dstar: InArg[float]
    Ks: InArg[float]
    N: InArg[float]
    modification: InArg[bool]
    variables_of_interest: InArg[list]

    epileptorCodim3: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.EpileptorCodim3)

    def execute(self, ctx) -> None:
        epileptorCodim3 = self.EpileptorCodim3()

        set_values(self, epileptorCodim3)
        self.epileptorCodim3.value = epileptorCodim3
        print_component_summary(self.epileptorCodim3.value)


@xai_component(color='rgb(101, 179, 46)')
class EpileptorCodim3SlowMod(Component):
    from tvb.simulator.models.epileptorcodim3 import EpileptorCodim3SlowMod
    mu1_Ain: InArg[float]
    mu2_Ain: InArg[float]
    nu_Ain: InArg[float]
    mu1_Bin: InArg[float]
    mu2_Bin: InArg[float]
    nu_Bin: InArg[float]
    mu1_Aend: InArg[float]
    mu2_Aend: InArg[float]
    nu_Aend: InArg[float]
    mu1_Bend: InArg[float]
    mu2_Bend: InArg[float]
    nu_Bend: InArg[float]
    b: InArg[float]
    R: InArg[float]
    c: InArg[float]
    cA: InArg[float]
    cB: InArg[float]
    dstar: InArg[float]
    Ks: InArg[float]
    N: InArg[float]
    modification: InArg[bool]
    variables_of_interest: InArg[list]

    epileptorCodim3SlowMod: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.EpileptorCodim3SlowMod)

    def execute(self, ctx) -> None:
        epileptorCodim3SlowMod = self.EpileptorCodim3SlowMod()

        set_values(self, epileptorCodim3SlowMod)
        self.epileptorCodim3SlowMod.value = epileptorCodim3SlowMod
        print_component_summary(self.epileptorCodim3SlowMod.value)
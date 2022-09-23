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
    mu1_start: InArg[list]
    mu2_start: InArg[list]
    nu_start: InArg[list]
    mu1_stop: InArg[list]
    mu2_stop: InArg[list]
    nu_stop: InArg[list]
    b: InArg[list]
    R: InArg[list]
    c: InArg[list]
    dstar: InArg[list]
    Ks: InArg[list]
    N: InArg[list]
    modification: InArg[list]
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
    mu1_Ain: InArg[list]
    mu2_Ain: InArg[list]
    nu_Ain: InArg[list]
    mu1_Bin: InArg[list]
    mu2_Bin: InArg[list]
    nu_Bin: InArg[list]
    mu1_Aend: InArg[list]
    mu2_Aend: InArg[list]
    nu_Aend: InArg[list]
    mu1_Bend: InArg[list]
    mu2_Bend: InArg[list]
    nu_Bend: InArg[list]
    b: InArg[list]
    R: InArg[list]
    c: InArg[list]
    cA: InArg[list]
    cB: InArg[list]
    dstar: InArg[list]
    Ks: InArg[list]
    N: InArg[list]
    modification: InArg[list]
    variables_of_interest: InArg[list]

    epileptorCodim3SlowMod: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.EpileptorCodim3SlowMod)

    def execute(self, ctx) -> None:
        epileptorCodim3SlowMod = self.EpileptorCodim3SlowMod()

        set_values(self, epileptorCodim3SlowMod)
        self.epileptorCodim3SlowMod.value = epileptorCodim3SlowMod
        print_component_summary(self.epileptorCodim3SlowMod.value)
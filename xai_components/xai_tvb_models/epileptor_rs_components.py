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
class EpileptorRestingState(Component):
    from tvb.simulator.models.epileptor_rs import EpileptorRestingState
    a: InArg[list]
    b: InArg[list]
    c: InArg[list]
    d: InArg[list]
    r: InArg[list]
    s: InArg[list]
    x0: InArg[list]
    Iext: InArg[list]
    slope: InArg[list]
    Iext2: InArg[list]
    tau: InArg[list]
    aa: InArg[list]
    bb: InArg[list]
    Kvf: InArg[list]
    Kf: InArg[list]
    Ks: InArg[list]
    tt: InArg[list]
    tau_rs: InArg[list]
    I_rs: InArg[list]
    a_rs: InArg[list]
    b_rs: InArg[list]
    d_rs: InArg[list]
    e_rs: InArg[list]
    f_rs: InArg[list]
    alpha_rs: InArg[list]
    beta_rs: InArg[list]
    gamma_rs: InArg[list]
    K_rs: InArg[list]
    p: InArg[list]
    variables_of_interest: InArg[list]

    epileptorRestingState: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.EpileptorRestingState)

    def execute(self, ctx) -> None:
        epileptorRestingState = self.EpileptorRestingState()

        set_values(self, epileptorRestingState)
        self.epileptorRestingState.value = epileptorRestingState
        print_component_summary(self.epileptorRestingState.value)

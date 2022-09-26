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
class EpileptorRestingState(ComponentWithWidget):
    a: InArg[float]
    b: InArg[float]
    c: InArg[float]
    d: InArg[float]
    r: InArg[float]
    s: InArg[float]
    x0: InArg[float]
    Iext: InArg[float]
    slope: InArg[float]
    Iext2: InArg[float]
    tau: InArg[float]
    aa: InArg[float]
    bb: InArg[float]
    Kvf: InArg[float]
    Kf: InArg[float]
    Ks: InArg[float]
    tt: InArg[float]
    tau_rs: InArg[float]
    I_rs: InArg[float]
    a_rs: InArg[float]
    b_rs: InArg[float]
    d_rs: InArg[float]
    e_rs: InArg[float]
    f_rs: InArg[float]
    alpha_rs: InArg[float]
    beta_rs: InArg[float]
    gamma_rs: InArg[float]
    K_rs: InArg[float]
    p: InArg[float]
    variables_of_interest: InArg[list]

    epileptorRestingState: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.epileptor_rs import EpileptorRestingState
        return EpileptorRestingState

    def execute(self, ctx) -> None:
        epileptorRestingState = self.tvb_ht_class()

        set_values(self, epileptorRestingState)
        self.epileptorRestingState.value = epileptorRestingState
        print_component_summary(self.epileptorRestingState.value)

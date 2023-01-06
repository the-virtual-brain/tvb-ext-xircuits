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
class EpileptorRestingState(ComponentWithWidget):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    s: InArg[Union[float, numpy.ndarray]]
    x0: InArg[Union[float, numpy.ndarray]]
    Iext: InArg[Union[float, numpy.ndarray]]
    slope: InArg[Union[float, numpy.ndarray]]
    Iext2: InArg[Union[float, numpy.ndarray]]
    tau: InArg[Union[float, numpy.ndarray]]
    aa: InArg[Union[float, numpy.ndarray]]
    bb: InArg[Union[float, numpy.ndarray]]
    Kvf: InArg[Union[float, numpy.ndarray]]
    Kf: InArg[Union[float, numpy.ndarray]]
    Ks: InArg[Union[float, numpy.ndarray]]
    tt: InArg[Union[float, numpy.ndarray]]
    tau_rs: InArg[Union[float, numpy.ndarray]]
    I_rs: InArg[Union[float, numpy.ndarray]]
    a_rs: InArg[Union[float, numpy.ndarray]]
    b_rs: InArg[Union[float, numpy.ndarray]]
    d_rs: InArg[Union[float, numpy.ndarray]]
    e_rs: InArg[Union[float, numpy.ndarray]]
    f_rs: InArg[Union[float, numpy.ndarray]]
    alpha_rs: InArg[Union[float, numpy.ndarray]]
    beta_rs: InArg[Union[float, numpy.ndarray]]
    gamma_rs: InArg[Union[float, numpy.ndarray]]
    K_rs: InArg[Union[float, numpy.ndarray]]
    p: InArg[Union[float, numpy.ndarray]]
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

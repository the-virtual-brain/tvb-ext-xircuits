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
class EpileptorCodim3(ComponentWithWidget):
    mu1_start: InArg[Union[float, numpy.ndarray]]
    mu2_start: InArg[Union[float, numpy.ndarray]]
    nu_start: InArg[Union[float, numpy.ndarray]]
    mu1_stop: InArg[Union[float, numpy.ndarray]]
    mu2_stop: InArg[Union[float, numpy.ndarray]]
    nu_stop: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    R: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    dstar: InArg[Union[float, numpy.ndarray]]
    Ks: InArg[Union[float, numpy.ndarray]]
    N: InArg[Union[float, numpy.ndarray]]
    modification: InArg[Union[bool, numpy.ndarray]]
    variables_of_interest: InArg[list]

    epileptorCodim3: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.epileptorcodim3 import EpileptorCodim3
        return EpileptorCodim3

    def execute(self, ctx) -> None:
        epileptorCodim3 = self.tvb_ht_class()

        set_values(self, epileptorCodim3)
        self.epileptorCodim3.value = epileptorCodim3
        print_component_summary(self.epileptorCodim3.value)


@xai_component(color='rgb(101, 179, 46)')
class EpileptorCodim3SlowMod(ComponentWithWidget):
    mu1_Ain: InArg[Union[float, numpy.ndarray]]
    mu2_Ain: InArg[Union[float, numpy.ndarray]]
    nu_Ain: InArg[Union[float, numpy.ndarray]]
    mu1_Bin: InArg[Union[float, numpy.ndarray]]
    mu2_Bin: InArg[Union[float, numpy.ndarray]]
    nu_Bin: InArg[Union[float, numpy.ndarray]]
    mu1_Aend: InArg[Union[float, numpy.ndarray]]
    mu2_Aend: InArg[Union[float, numpy.ndarray]]
    nu_Aend: InArg[Union[float, numpy.ndarray]]
    mu1_Bend: InArg[Union[float, numpy.ndarray]]
    mu2_Bend: InArg[Union[float, numpy.ndarray]]
    nu_Bend: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    R: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    cA: InArg[Union[float, numpy.ndarray]]
    cB: InArg[Union[float, numpy.ndarray]]
    dstar: InArg[Union[float, numpy.ndarray]]
    Ks: InArg[Union[float, numpy.ndarray]]
    N: InArg[Union[float, numpy.ndarray]]
    modification: InArg[Union[bool, numpy.ndarray]]
    variables_of_interest: InArg[list]

    epileptorCodim3SlowMod: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.epileptorcodim3 import EpileptorCodim3SlowMod
        return EpileptorCodim3SlowMod

    def execute(self, ctx) -> None:
        epileptorCodim3SlowMod = self.tvb_ht_class()

        set_values(self, epileptorCodim3SlowMod)
        self.epileptorCodim3SlowMod.value = epileptorCodim3SlowMod
        print_component_summary(self.epileptorCodim3SlowMod.value)

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
class JansenRit(ComponentWithWidget):
    A: InArg[Union[float, numpy.ndarray]]
    B: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    v0: InArg[Union[float, numpy.ndarray]]
    nu_max: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    J: InArg[Union[float, numpy.ndarray]]
    a_1: InArg[Union[float, numpy.ndarray]]
    a_2: InArg[Union[float, numpy.ndarray]]
    a_3: InArg[Union[float, numpy.ndarray]]
    a_4: InArg[Union[float, numpy.ndarray]]
    p_min: InArg[Union[float, numpy.ndarray]]
    p_max: InArg[Union[float, numpy.ndarray]]
    mu: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    jansenRit: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.jansen_rit import JansenRit
        return JansenRit

    def execute(self, ctx) -> None:
        jansenRit = self.tvb_ht_class()

        set_values(self, jansenRit)
        self.jansenRit.value = jansenRit
        print_component_summary(self.jansenRit.value)


@xai_component(color='rgb(101, 179, 46)')
class ZetterbergJansen(ComponentWithWidget):
    He: InArg[Union[float, numpy.ndarray]]
    Hi: InArg[Union[float, numpy.ndarray]]
    ke: InArg[Union[float, numpy.ndarray]]
    ki: InArg[Union[float, numpy.ndarray]]
    e0: InArg[Union[float, numpy.ndarray]]
    rho_2: InArg[Union[float, numpy.ndarray]]
    rho_1: InArg[Union[float, numpy.ndarray]]
    gamma_1: InArg[Union[float, numpy.ndarray]]
    gamma_2: InArg[Union[float, numpy.ndarray]]
    gamma_3: InArg[Union[float, numpy.ndarray]]
    gamma_4: InArg[Union[float, numpy.ndarray]]
    gamma_5: InArg[Union[float, numpy.ndarray]]
    gamma_1T: InArg[Union[float, numpy.ndarray]]
    gamma_2T: InArg[Union[float, numpy.ndarray]]
    gamma_3T: InArg[Union[float, numpy.ndarray]]
    P: InArg[Union[float, numpy.ndarray]]
    U: InArg[Union[float, numpy.ndarray]]
    Q: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    zetterbergJansen: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.jansen_rit import ZetterbergJansen
        return ZetterbergJansen

    def execute(self, ctx) -> None:
        zetterbergJansen = self.tvb_ht_class()

        set_values(self, zetterbergJansen)
        self.zetterbergJansen.value = zetterbergJansen
        print_component_summary(self.zetterbergJansen.value)

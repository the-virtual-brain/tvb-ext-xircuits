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
class JansenRit(ComponentWithWidget):
    A: InArg[float]
    B: InArg[float]
    a: InArg[float]
    b: InArg[float]
    v0: InArg[float]
    nu_max: InArg[float]
    r: InArg[float]
    J: InArg[float]
    a_1: InArg[float]
    a_2: InArg[float]
    a_3: InArg[float]
    a_4: InArg[float]
    p_min: InArg[float]
    p_max: InArg[float]
    mu: InArg[float]
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
    He: InArg[float]
    Hi: InArg[float]
    ke: InArg[float]
    ki: InArg[float]
    e0: InArg[float]
    rho_2: InArg[float]
    rho_1: InArg[float]
    gamma_1: InArg[float]
    gamma_2: InArg[float]
    gamma_3: InArg[float]
    gamma_4: InArg[float]
    gamma_5: InArg[float]
    gamma_1T: InArg[float]
    gamma_2T: InArg[float]
    gamma_3T: InArg[float]
    P: InArg[float]
    U: InArg[float]
    Q: InArg[float]
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

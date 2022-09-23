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
class JansenRit(Component):
    from tvb.simulator.models.jansen_rit import JansenRit
    A: InArg[list]
    B: InArg[list]
    a: InArg[list]
    b: InArg[list]
    v0: InArg[list]
    nu_max: InArg[list]
    r: InArg[list]
    J: InArg[list]
    a_1: InArg[list]
    a_2: InArg[list]
    a_3: InArg[list]
    a_4: InArg[list]
    p_min: InArg[list]
    p_max: InArg[list]
    mu: InArg[list]
    variables_of_interest: InArg[list]

    jansenRit: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.JansenRit)

    def execute(self, ctx) -> None:
        jansenRit = self.JansenRit()

        set_values(self, jansenRit)
        self.jansenRit.value = jansenRit
        print_component_summary(self.jansenRit.value)


@xai_component(color='rgb(101, 179, 46)')
class ZetterbergJansen(Component):
    from tvb.simulator.models.jansen_rit import ZetterbergJansen
    He: InArg[list]
    Hi: InArg[list]
    ke: InArg[list]
    ki: InArg[list]
    e0: InArg[list]
    rho_2: InArg[list]
    rho_1: InArg[list]
    gamma_1: InArg[list]
    gamma_2: InArg[list]
    gamma_3: InArg[list]
    gamma_4: InArg[list]
    gamma_5: InArg[list]
    gamma_1T: InArg[list]
    gamma_2T: InArg[list]
    gamma_3T: InArg[list]
    P: InArg[list]
    U: InArg[list]
    Q: InArg[list]
    variables_of_interest: InArg[list]

    zetterbergJansen: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ZetterbergJansen)

    def execute(self, ctx) -> None:
        zetterbergJansen = self.ZetterbergJansen()

        set_values(self, zetterbergJansen)
        self.zetterbergJansen.value = zetterbergJansen
        print_component_summary(self.zetterbergJansen.value)
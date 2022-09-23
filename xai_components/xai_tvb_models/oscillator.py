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
class Generic2dOscillator(Component):
    from tvb.simulator.models.oscillator import Generic2dOscillator
    tau: InArg[list]
    I: InArg[list]
    a: InArg[list]
    b: InArg[list]
    c: InArg[list]
    d: InArg[list]
    e: InArg[list]
    f: InArg[list]
    g: InArg[list]
    alpha: InArg[list]
    beta: InArg[list]
    gamma: InArg[list]
    variables_of_interest: InArg[list]

    generic2doscillator: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Generic2dOscillator)

    def execute(self, ctx) -> None:
        generic2doscillator = self.Generic2dOscillator()

        set_values(self, generic2doscillator)
        self.generic2doscillator.value = generic2doscillator
        print_component_summary(self.generic2doscillator.value)


@xai_component(color='rgb(101, 179, 46)')
class Kuramoto(Component):
    from tvb.simulator.models.oscillator import Kuramoto
    omega: InArg[list]
    variables_of_interest: InArg[list]

    kuramoto: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Kuramoto)

    def execute(self, ctx) -> None:
        kuramoto = self.Kuramoto()

        set_values(self, kuramoto)
        self.kuramoto.value = kuramoto
        print_component_summary(self.kuramoto.value)


@xai_component(color='rgb(101, 179, 46)')
class SupHopf(Component):
    from tvb.simulator.models.oscillator import SupHopf
    a: InArg[list]
    omega: InArg[list]
    variables_of_interest: InArg[list]

    suphopf: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.SupHopf)

    def execute(self, ctx) -> None:
        suphopf = self.SupHopf()

        set_values(self, suphopf)
        self.suphopf.value = suphopf
        print_component_summary(self.suphopf.value)
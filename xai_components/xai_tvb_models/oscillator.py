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
    tau: InArg[float]
    I: InArg[float]
    a: InArg[float]
    b: InArg[float]
    c: InArg[float]
    d: InArg[float]
    e: InArg[float]
    f: InArg[float]
    g: InArg[float]
    alpha: InArg[float]
    beta: InArg[float]
    gamma: InArg[float]
    variables_of_interest: InArg[list]

    generic2dOscillator: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Generic2dOscillator)

    def execute(self, ctx) -> None:
        generic2dOscillator = self.Generic2dOscillator()

        set_values(self, generic2dOscillator)
        self.generic2dOscillator.value = generic2dOscillator
        print_component_summary(self.generic2dOscillator.value)


@xai_component(color='rgb(101, 179, 46)')
class Kuramoto(Component):
    from tvb.simulator.models.oscillator import Kuramoto
    omega: InArg[float]
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
    a: InArg[float]
    omega: InArg[float]
    variables_of_interest: InArg[list]

    supHopf: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.SupHopf)

    def execute(self, ctx) -> None:
        supHopf = self.SupHopf()

        set_values(self, supHopf)
        self.supHopf.value = supHopf
        print_component_summary(self.supHopf.value)
# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from numpy.random import RandomState
from tvb.simulator.noise import Noise

from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class Additive(Component):
    from tvb.simulator.noise import Additive
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[RandomState]
    nsig: InArg[list]

    additive: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.Additive)

    def execute(self, ctx) -> None:
        additive = self.Additive()

        set_values(self, additive)
        self.additive.value = additive
        print_component_summary(self.additive.value)


@xai_component(color='rgb(253, 225, 0)')
class Multiplicative(Component):
    from tvb.simulator.noise import Multiplicative
    from tvb.datatypes.equations import TemporalApplicableEquation
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[RandomState]
    nsig: InArg[float]
    b: InArg[TemporalApplicableEquation]

    multiplicative: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.Multiplicative)

    def execute(self, ctx) -> None:
        multiplicative = self.Multiplicative()

        set_values(self, multiplicative)
        self.multiplicative.value = multiplicative
        print_component_summary(self.multiplicative.value)


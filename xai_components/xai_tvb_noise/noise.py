# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from numpy.random import RandomState
from tvb.simulator.noise import Noise

from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class Additive(TVBComponent):
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[RandomState]
    nsig: InArg[float]

    additive: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.noise import Additive
        return Additive

    def execute(self, ctx) -> None:
        additive = self.tvb_ht_class()

        set_values(self, additive)
        self.additive.value = additive
        print_component_summary(self.additive.value)


@xai_component(color='rgb(253, 225, 0)')
class Multiplicative(TVBComponent):
    from tvb.datatypes.equations import TemporalApplicableEquation
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[RandomState]
    nsig: InArg[float]
    b: InArg[TemporalApplicableEquation]

    multiplicative: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.noise import Multiplicative
        return Multiplicative

    def execute(self, ctx) -> None:
        multiplicative = self.tvb_ht_class()

        set_values(self, multiplicative)
        self.multiplicative.value = multiplicative
        print_component_summary(self.multiplicative.value)


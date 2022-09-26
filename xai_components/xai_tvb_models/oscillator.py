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
class Generic2dOscillator(ComponentWithWidget):
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

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.oscillator import Generic2dOscillator
        return Generic2dOscillator

    def execute(self, ctx) -> None:
        generic2dOscillator = self.tvb_ht_class()

        set_values(self, generic2dOscillator)
        self.generic2dOscillator.value = generic2dOscillator
        print_component_summary(self.generic2dOscillator.value)


@xai_component(color='rgb(101, 179, 46)')
class Kuramoto(ComponentWithWidget):
    omega: InArg[float]
    variables_of_interest: InArg[list]

    kuramoto: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.oscillator import Kuramoto
        return Kuramoto

    def execute(self, ctx) -> None:
        kuramoto = self.tvb_ht_class()

        set_values(self, kuramoto)
        self.kuramoto.value = kuramoto
        print_component_summary(self.kuramoto.value)


@xai_component(color='rgb(101, 179, 46)')
class SupHopf(ComponentWithWidget):
    a: InArg[float]
    omega: InArg[float]
    variables_of_interest: InArg[list]

    supHopf: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.oscillator import SupHopf
        return SupHopf

    def execute(self, ctx) -> None:
        supHopf = self.tvb_ht_class()

        set_values(self, supHopf)
        self.supHopf.value = supHopf
        print_component_summary(self.supHopf.value)

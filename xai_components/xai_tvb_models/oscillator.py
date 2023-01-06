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
class Generic2dOscillator(ComponentWithWidget):
    tau: InArg[Union[float, numpy.ndarray]]
    I: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    e: InArg[Union[float, numpy.ndarray]]
    f: InArg[Union[float, numpy.ndarray]]
    g: InArg[Union[float, numpy.ndarray]]
    alpha: InArg[Union[float, numpy.ndarray]]
    beta: InArg[Union[float, numpy.ndarray]]
    gamma: InArg[Union[float, numpy.ndarray]]
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
    omega: InArg[Union[float, numpy.ndarray]]
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
    a: InArg[Union[float, numpy.ndarray]]
    omega: InArg[Union[float, numpy.ndarray]]
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

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
class ReducedSetFitzHughNagumo(ComponentWithWidget):
    tau: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    K11: InArg[Union[float, numpy.ndarray]]
    K12: InArg[Union[float, numpy.ndarray]]
    K21: InArg[Union[float, numpy.ndarray]]
    sigma: InArg[Union[float, numpy.ndarray]]
    mu: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    reducedSetFitzHughNagumo: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.stefanescu_jirsa import ReducedSetFitzHughNagumo
        return ReducedSetFitzHughNagumo

    def execute(self, ctx) -> None:
        reducedSetFitzHughNagumo = self.tvb_ht_class()

        set_values(self, reducedSetFitzHughNagumo)
        self.reducedSetFitzHughNagumo.value = reducedSetFitzHughNagumo
        print_component_summary(self.reducedSetFitzHughNagumo.value)


@xai_component(color='rgb(101, 179, 46)')
class ReducedSetHindmarshRose(ComponentWithWidget):
    r: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    s: InArg[Union[float, numpy.ndarray]]
    xo: InArg[Union[float, numpy.ndarray]]
    K11: InArg[Union[float, numpy.ndarray]]
    K12: InArg[Union[float, numpy.ndarray]]
    K21: InArg[Union[float, numpy.ndarray]]
    sigma: InArg[Union[float, numpy.ndarray]]
    mu: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]

    reducedSetHindmarshRose: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.stefanescu_jirsa import ReducedSetHindmarshRose
        return ReducedSetHindmarshRose

    def execute(self, ctx) -> None:
        reducedSetHindmarshRose = self.tvb_ht_class()

        set_values(self, reducedSetHindmarshRose)
        self.reducedSetHindmarshRose.value = reducedSetHindmarshRose
        print_component_summary(self.reducedSetHindmarshRose.value)

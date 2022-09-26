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
class ReducedSetFitzHughNagumo(ComponentWithWidget):
    tau: InArg[float]
    a: InArg[float]
    b: InArg[float]
    K11: InArg[float]
    K12: InArg[float]
    K21: InArg[float]
    sigma: InArg[float]
    mu: InArg[float]
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
    r: InArg[float]
    a: InArg[float]
    b: InArg[float]
    c: InArg[float]
    d: InArg[float]
    s: InArg[float]
    xo: InArg[float]
    K11: InArg[float]
    K12: InArg[float]
    K21: InArg[float]
    sigma: InArg[float]
    mu: InArg[float]
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

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
class ReducedSetFitzHughNagumo(Component):
    from tvb.simulator.models.stefanescu_jirsa import ReducedSetFitzHughNagumo
    tau: InArg[list]
    a: InArg[list]
    b: InArg[list]
    K11: InArg[list]
    K12: InArg[list]
    K21: InArg[list]
    sigma: InArg[list]
    mu: InArg[list]
    variables_of_interest: InArg[list]

    reducedSetFitzHughNagumo: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ReducedSetFitzHughNagumo)

    def execute(self, ctx) -> None:
        reducedSetFitzHughNagumo = self.ReducedSetFitzHughNagumo()

        set_values(self, reducedSetFitzHughNagumo)
        self.reducedSetFitzHughNagumo.value = reducedSetFitzHughNagumo
        print_component_summary(self.reducedSetFitzHughNagumo.value)


@xai_component(color='rgb(101, 179, 46)')
class ReducedSetHindmarshRose(Component):
    from tvb.simulator.models.stefanescu_jirsa import ReducedSetHindmarshRose
    r: InArg[list]
    a: InArg[list]
    b: InArg[list]
    c: InArg[list]
    d: InArg[list]
    s: InArg[list]
    xo: InArg[list]
    K11: InArg[list]
    K12: InArg[list]
    K21: InArg[list]
    sigma: InArg[list]
    mu: InArg[list]
    variables_of_interest: InArg[list]

    reducedSetHindmarshRose: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.ReducedSetHindmarshRose)

    def execute(self, ctx) -> None:
        reducedSetHindmarshRose = self.ReducedSetHindmarshRose()

        set_values(self, reducedSetHindmarshRose)
        self.reducedSetHindmarshRose.value = reducedSetHindmarshRose
        print_component_summary(self.reducedSetHindmarshRose.value)
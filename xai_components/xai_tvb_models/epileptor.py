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
class Epileptor(Component):
    from tvb.simulator.models.epileptor import Epileptor
    a: InArg[float]
    b: InArg[float]
    c: InArg[float]
    d: InArg[float]
    r: InArg[float]
    s: InArg[float]
    x0: InArg[float]
    Iext: InArg[float]
    slope: InArg[float]
    Iext2: InArg[float]
    tau: InArg[float]
    aa: InArg[float]
    bb: InArg[float]
    Kvf: InArg[float]
    Kf: InArg[float]
    Ks: InArg[float]
    tt: InArg[float]
    modification: InArg[bool]
    variables_of_interest: InArg[list]

    epileptor: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Epileptor)

    def execute(self, ctx) -> None:
        epileptor = self.Epileptor()

        set_values(self, epileptor)
        self.epileptor.value = epileptor
        print_component_summary(self.epileptor.value)


@xai_component(color='rgb(101, 179, 46)')
class Epileptor2D(Component):
    from tvb.simulator.models.epileptor import Epileptor2D
    a: InArg[float]
    b: InArg[float]
    c: InArg[float]
    d: InArg[float]
    r: InArg[float]
    x0: InArg[float]
    Iext: InArg[float]
    slope: InArg[float]
    Kvf: InArg[float]
    Ks: InArg[float]
    tt: InArg[float]
    modification: InArg[bool]
    variables_of_interest: InArg[list]

    epileptor2D: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Epileptor2D)

    def execute(self, ctx) -> None:
        epileptor2D = self.Epileptor2D()

        set_values(self, epileptor2D)
        self.epileptor2D.value = epileptor2D
        print_component_summary(self.epileptor2D.value)

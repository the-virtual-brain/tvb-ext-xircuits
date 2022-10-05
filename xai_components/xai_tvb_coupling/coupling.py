# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.coupling import Coupling
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(0, 102, 178)')
class LinearCoupling(Component):
    from tvb.simulator.coupling import Linear
    a: InArg[float]
    b: InArg[float]

    linear: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.Linear)

    def execute(self, ctx) -> None:
        linear = self.Linear()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)


@xai_component(color='rgb(0, 102, 178)')
class Scaling(Component):
    from tvb.simulator.coupling import Scaling
    a: InArg[float]

    scaling: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.Scaling)

    def execute(self, ctx) -> None:
        scaling = self.Scaling()

        set_values(self, scaling)
        self.scaling.value = scaling
        print_component_summary(self.scaling.value)


@xai_component(color='rgb(0, 102, 178)')
class HyperbolicTangent(Component):
    from tvb.simulator.coupling import HyperbolicTangent
    a: InArg[float]
    b: InArg[float]
    midpoint: InArg[float]
    sigma: InArg[float]

    hyperbolicTangent: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.HyperbolicTangent)

    def execute(self, ctx) -> None:
        hyperbolicTangent = self.HyperbolicTangent()

        set_values(self, hyperbolicTangent)
        self.hyperbolicTangent.value = hyperbolicTangent
        print_component_summary(self.hyperbolicTangent.value)


@xai_component(color='rgb(0, 102, 178)')
class Sigmoidal(Component):
    from tvb.simulator.coupling import Sigmoidal
    cmin: InArg[float]
    cmax: InArg[float]
    midpoint: InArg[float]
    a: InArg[float]
    sigma: InArg[float]

    sigmoidal: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.Sigmoidal)

    def execute(self, ctx) -> None:
        sigmoidal = self.Sigmoidal()

        set_values(self, sigmoidal)
        self.sigmoidal.value = sigmoidal
        print_component_summary(self.sigmoidal.value)


@xai_component(color='rgb(0, 102, 178)')
class SigmoidalJansenRit(Component):
    from tvb.simulator.coupling import SigmoidalJansenRit
    cmin: InArg[float]
    cmax: InArg[float]
    midpoint: InArg[float]
    r: InArg[float]
    a: InArg[float]

    sigmoidalJansenRit: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.SigmoidalJansenRit)

    def execute(self, ctx) -> None:
        sigmoidalJansenRit = self.SigmoidalJansenRit()

        set_values(self, sigmoidalJansenRit)
        self.sigmoidalJansenRit.value = sigmoidalJansenRit
        print_component_summary(self.sigmoidalJansenRit.value)


@xai_component(color='rgb(0, 102, 178)')
class PreSigmoidal(Component):
    from tvb.simulator.coupling import PreSigmoidal
    H: InArg[float]
    Q: InArg[float]
    G: InArg[float]
    P: InArg[float]
    theta: InArg[float]
    dynamic: InArg[bool]
    globalT: InArg[bool]

    preSigmoidal: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.PreSigmoidal)

    def execute(self, ctx) -> None:
        preSigmoidal = self.PreSigmoidal()

        set_values(self, preSigmoidal)
        self.preSigmoidal.value = preSigmoidal
        print_component_summary(self.preSigmoidal.value)


@xai_component(color='rgb(0, 102, 178)')
class Difference(Component):
    from tvb.simulator.coupling import Difference
    a: InArg[float]

    difference: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.Difference)

    def execute(self, ctx) -> None:
        difference = self.Difference()

        set_values(self, difference)
        self.difference.value = difference
        print_component_summary(self.difference.value)


@xai_component(color='rgb(0, 102, 178)')
class KuramotoCoupling(Component):
    from tvb.simulator.coupling import Kuramoto
    a: InArg[float]

    kuramoto: OutArg[Coupling]

    def __init__(self):
        set_defaults(self, self.Kuramoto)

    def execute(self, ctx) -> None:
        kuramoto = self.Kuramoto()

        set_values(self, kuramoto)
        self.kuramoto.value = kuramoto
        print_component_summary(self.kuramoto.value)


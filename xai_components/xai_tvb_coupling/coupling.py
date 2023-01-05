# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy
from tvb.simulator.coupling import Coupling
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(0, 102, 178)')
class LinearCoupling(TVBComponent):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]

    linear: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import Linear
        return Linear

    def execute(self, ctx) -> None:
        linear = self.tvb_ht_class()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)


@xai_component(color='rgb(0, 102, 178)')
class Scaling(TVBComponent):
    a: InArg[Union[float, numpy.ndarray]]

    scaling: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import Scaling
        return Scaling

    def execute(self, ctx) -> None:
        scaling = self.tvb_ht_class()

        set_values(self, scaling)
        self.scaling.value = scaling
        print_component_summary(self.scaling.value)


@xai_component(color='rgb(0, 102, 178)')
class HyperbolicTangent(TVBComponent):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    midpoint: InArg[Union[float, numpy.ndarray]]
    sigma: InArg[Union[float, numpy.ndarray]]

    hyperbolicTangent: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import HyperbolicTangent
        return HyperbolicTangent

    def execute(self, ctx) -> None:
        hyperbolicTangent = self.tvb_ht_class()

        set_values(self, hyperbolicTangent)
        self.hyperbolicTangent.value = hyperbolicTangent
        print_component_summary(self.hyperbolicTangent.value)


@xai_component(color='rgb(0, 102, 178)')
class Sigmoidal(TVBComponent):
    cmin: InArg[Union[float, numpy.ndarray]]
    cmax: InArg[Union[float, numpy.ndarray]]
    midpoint: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    sigma: InArg[Union[float, numpy.ndarray]]

    sigmoidal: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import Sigmoidal
        return Sigmoidal

    def execute(self, ctx) -> None:
        sigmoidal = self.tvb_ht_class()

        set_values(self, sigmoidal)
        self.sigmoidal.value = sigmoidal
        print_component_summary(self.sigmoidal.value)


@xai_component(color='rgb(0, 102, 178)')
class SigmoidalJansenRit(TVBComponent):
    cmin: InArg[Union[float, numpy.ndarray]]
    cmax: InArg[Union[float, numpy.ndarray]]
    midpoint: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]

    sigmoidalJansenRit: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import SigmoidalJansenRit
        return SigmoidalJansenRit

    def execute(self, ctx) -> None:
        sigmoidalJansenRit = self.tvb_ht_class()

        set_values(self, sigmoidalJansenRit)
        self.sigmoidalJansenRit.value = sigmoidalJansenRit
        print_component_summary(self.sigmoidalJansenRit.value)


@xai_component(color='rgb(0, 102, 178)')
class PreSigmoidal(TVBComponent):
    H: InArg[Union[float, numpy.ndarray]]
    Q: InArg[Union[float, numpy.ndarray]]
    G: InArg[Union[float, numpy.ndarray]]
    P: InArg[Union[float, numpy.ndarray]]
    theta: InArg[Union[float, numpy.ndarray]]
    dynamic: InArg[bool]
    globalT: InArg[bool]

    preSigmoidal: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import PreSigmoidal
        return PreSigmoidal

    def execute(self, ctx) -> None:
        preSigmoidal = self.tvb_ht_class()

        set_values(self, preSigmoidal)
        self.preSigmoidal.value = preSigmoidal
        print_component_summary(self.preSigmoidal.value)


@xai_component(color='rgb(0, 102, 178)')
class Difference(TVBComponent):
    a: InArg[Union[float, numpy.ndarray]]

    difference: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import Difference
        return Difference

    def execute(self, ctx) -> None:
        difference = self.tvb_ht_class()

        set_values(self, difference)
        self.difference.value = difference
        print_component_summary(self.difference.value)


@xai_component(color='rgb(0, 102, 178)')
class KuramotoCoupling(TVBComponent):
    a: InArg[Union[float, numpy.ndarray]]

    kuramoto: OutArg[Coupling]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.coupling import Kuramoto
        return Kuramoto

    def execute(self, ctx) -> None:
        kuramoto = self.tvb_ht_class()

        set_values(self, kuramoto)
        self.kuramoto.value = kuramoto
        print_component_summary(self.kuramoto.value)

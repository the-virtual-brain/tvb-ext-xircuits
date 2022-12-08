# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.equations import Equation

from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class DiscreteEquation(TVBComponent):
    parameters: InArg[dict]

    discreteEquation: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import DiscreteEquation
        return DiscreteEquation

    def execute(self, ctx) -> None:
        discreteEquation = self.tvb_ht_class()

        set_values(self, discreteEquation)
        self.discreteEquation.value = discreteEquation
        print_component_summary(self.discreteEquation.value)


@xai_component(color='rgb(253, 225, 0)')
class LinearEquation(TVBComponent):
    parameters: InArg[dict]

    linear: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Linear
        return Linear

    def execute(self, ctx) -> None:
        linear = self.tvb_ht_class()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)


@xai_component(color='rgb(253, 225, 0)')
class Gaussian(TVBComponent):
    parameters: InArg[dict]

    gaussian: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Gaussian
        return Gaussian

    def execute(self, ctx) -> None:
        gaussian = self.tvb_ht_class()

        set_values(self, gaussian)
        self.gaussian.value = gaussian
        print_component_summary(self.gaussian.value)


@xai_component(color='rgb(253, 225, 0)')
class DoubleGaussian(TVBComponent):
    parameters: InArg[dict]

    doubleGaussian: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import DoubleGaussian
        return DoubleGaussian

    def execute(self, ctx) -> None:
        doubleGaussian = self.tvb_ht_class()

        set_values(self, doubleGaussian)
        self.doubleGaussian.value = doubleGaussian
        print_component_summary(self.doubleGaussian.value)


@xai_component(color='rgb(253, 225, 0)')
class Sigmoid(TVBComponent):
    parameters: InArg[dict]

    sigmoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Sigmoid
        return Sigmoid

    def execute(self, ctx) -> None:
        sigmoid = self.tvb_ht_class()

        set_values(self, sigmoid)
        self.sigmoid.value = sigmoid
        print_component_summary(self.sigmoid.value)


@xai_component(color='rgb(253, 225, 0)')
class GeneralizedSigmoid(TVBComponent):
    parameters: InArg[dict]

    generalizedSigmoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import GeneralizedSigmoid
        return GeneralizedSigmoid

    def execute(self, ctx) -> None:
        generalizedSigmoid = self.tvb_ht_class()

        set_values(self, generalizedSigmoid)
        self.generalizedSigmoid.value = generalizedSigmoid
        print_component_summary(self.generalizedSigmoid.value)


@xai_component(color='rgb(253, 225, 0)')
class Sinusoid(TVBComponent):
    parameters: InArg[dict]

    sinusoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Sinusoid
        return Sinusoid

    def execute(self, ctx) -> None:
        sinusoid = self.tvb_ht_class()

        set_values(self, sinusoid)
        self.sinusoid.value = sinusoid
        print_component_summary(self.sinusoid.value)


@xai_component(color='rgb(253, 225, 0)')
class Cosine(TVBComponent):
    parameters: InArg[dict]

    cosine: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Cosine
        return Cosine

    def execute(self, ctx) -> None:
        cosine = self.tvb_ht_class()

        set_values(self, cosine)
        self.cosine.value = cosine
        print_component_summary(self.cosine.value)


@xai_component(color='rgb(253, 225, 0)')
class Alpha(TVBComponent):
    parameters: InArg[dict]

    alpha: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Alpha
        return Alpha

    def execute(self, ctx) -> None:
        alpha = self.tvb_ht_class()

        set_values(self, alpha)
        self.alpha.value = alpha
        print_component_summary(self.alpha.value)


@xai_component(color='rgb(253, 225, 0)')
class PulseTrain(TVBComponent):
    parameters: InArg[dict]

    pulseTrain: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import PulseTrain
        return PulseTrain


    def execute(self, ctx) -> None:
        pulseTrain = self.tvb_ht_class()

        set_values(self, pulseTrain)
        self.pulseTrain.value = pulseTrain
        print_component_summary(self.pulseTrain.value)


@xai_component(color='rgb(253, 225, 0)')
class Gamma(TVBComponent):
    parameters: InArg[dict]

    gamma: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import Gamma
        return Gamma

    def execute(self, ctx) -> None:
        gamma = self.tvb_ht_class()

        set_values(self, gamma)
        self.gamma.value = gamma
        print_component_summary(self.gamma.value)


@xai_component(color='rgb(253, 225, 0)')
class DoubleExponential(TVBComponent):
    parameters: InArg[dict]

    doubleExponential: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import DoubleExponential
        return DoubleExponential


    def execute(self, ctx) -> None:
        doubleExponential = self.tvb_ht_class()

        set_values(self, doubleExponential)
        self.doubleExponential.value = doubleExponential
        print_component_summary(self.doubleExponential.value)


@xai_component(color='rgb(253, 225, 0)')
class FirstOrderVolterra(TVBComponent):
    parameters: InArg[dict]

    firstOrderVolterra: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import FirstOrderVolterra
        return FirstOrderVolterra

    def execute(self, ctx) -> None:
        firstOrderVolterra = self.tvb_ht_class()

        set_values(self, firstOrderVolterra)
        self.firstOrderVolterra.value = firstOrderVolterra
        print_component_summary(self.firstOrderVolterra.value)


@xai_component(color='rgb(253, 225, 0)')
class MixtureOfGammas(TVBComponent):
    parameters: InArg[dict]

    mixtureOfGammas: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.equations import MixtureOfGammas
        return MixtureOfGammas

    def execute(self, ctx) -> None:
        mixtureOfGammas = self.tvb_ht_class()

        set_values(self, mixtureOfGammas)
        self.mixtureOfGammas.value = mixtureOfGammas
        print_component_summary(self.mixtureOfGammas.value)

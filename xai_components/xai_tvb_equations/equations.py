# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.equations import Equation

from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class LinearEquation(Component):
    from tvb.datatypes.equations import Linear
    parameters: InArg[dict]

    linear: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Linear)

    def execute(self, ctx) -> None:
        linear = self.Linear()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)


@xai_component(color='rgb(253, 225, 0)')
class Gaussian(Component):
    from tvb.datatypes.equations import Gaussian
    parameters: InArg[dict]

    gaussian: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Gaussian)

    def execute(self, ctx) -> None:
        gaussian = self.Gaussian()

        set_values(self, gaussian)
        self.gaussian.value = gaussian
        print_component_summary(self.gaussian.value)


@xai_component(color='rgb(253, 225, 0)')
class DoubleGaussian(Component):
    from tvb.datatypes.equations import DoubleGaussian
    parameters: InArg[dict]

    doubleGaussian: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.DoubleGaussian)

    def execute(self, ctx) -> None:
        doubleGaussian = self.DoubleGaussian()

        set_values(self, doubleGaussian)
        self.doubleGaussian.value = doubleGaussian
        print_component_summary(self.doubleGaussian.value)


@xai_component(color='rgb(253, 225, 0)')
class Sigmoid(Component):
    from tvb.datatypes.equations import Sigmoid
    parameters: InArg[dict]

    sigmoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Sigmoid)

    def execute(self, ctx) -> None:
        sigmoid = self.Sigmoid()

        set_values(self, sigmoid)
        self.sigmoid.value = sigmoid
        print_component_summary(self.sigmoid.value)


@xai_component(color='rgb(253, 225, 0)')
class GeneralizedSigmoid(Component):
    from tvb.datatypes.equations import GeneralizedSigmoid
    parameters: InArg[dict]

    generalizedSigmoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.GeneralizedSigmoid)

    def execute(self, ctx) -> None:
        generalizedSigmoid = self.GeneralizedSigmoid()

        set_values(self, generalizedSigmoid)
        self.generalizedSigmoid.value = generalizedSigmoid
        print_component_summary(self.generalizedSigmoid.value)


@xai_component(color='rgb(253, 225, 0)')
class Sinusoid(Component):
    from tvb.datatypes.equations import Sinusoid
    parameters: InArg[dict]

    sinusoid: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Sinusoid)

    def execute(self, ctx) -> None:
        sinusoid = self.Sinusoid()

        set_values(self, sinusoid)
        self.sinusoid.value = sinusoid
        print_component_summary(self.sinusoid.value)


@xai_component(color='rgb(253, 225, 0)')
class Cosine(Component):
    from tvb.datatypes.equations import Cosine
    parameters: InArg[dict]

    cosine: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Cosine)

    def execute(self, ctx) -> None:
        cosine = self.Cosine()

        set_values(self, cosine)
        self.cosine.value = cosine
        print_component_summary(self.cosine.value)


@xai_component(color='rgb(253, 225, 0)')
class Alpha(Component):
    from tvb.datatypes.equations import Alpha
    parameters: InArg[dict]

    alpha: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Alpha)

    def execute(self, ctx) -> None:
        alpha = self.Alpha()

        set_values(self, alpha)
        self.alpha.value = alpha
        print_component_summary(self.alpha.value)


@xai_component(color='rgb(253, 225, 0)')
class PulseTrain(Component):
    from tvb.datatypes.equations import PulseTrain
    parameters: InArg[dict]

    pulseTrain: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.PulseTrain)

    def execute(self, ctx) -> None:
        pulseTrain = self.PulseTrain()

        set_values(self, pulseTrain)
        self.pulseTrain.value = pulseTrain
        print_component_summary(self.pulseTrain.value)


@xai_component(color='rgb(253, 225, 0)')
class Gamma(Component):
    from tvb.datatypes.equations import Gamma
    parameters: InArg[dict]

    gamma: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.Gamma)

    def execute(self, ctx) -> None:
        gamma = self.Gamma()

        set_values(self, gamma)
        self.gamma.value = gamma
        print_component_summary(self.gamma.value)


@xai_component(color='rgb(253, 225, 0)')
class DoubleExponential(Component):
    from tvb.datatypes.equations import DoubleExponential
    parameters: InArg[dict]

    doubleExponential: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.DoubleExponential)

    def execute(self, ctx) -> None:
        doubleExponential = self.DoubleExponential()

        set_values(self, doubleExponential)
        self.doubleExponential.value = doubleExponential
        print_component_summary(self.doubleExponential.value)


@xai_component(color='rgb(253, 225, 0)')
class FirstOrderVolterra(Component):
    from tvb.datatypes.equations import FirstOrderVolterra
    parameters: InArg[dict]

    firstOrderVolterra: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.FirstOrderVolterra)

    def execute(self, ctx) -> None:
        firstOrderVolterra = self.FirstOrderVolterra()

        set_values(self, firstOrderVolterra)
        self.firstOrderVolterra.value = firstOrderVolterra
        print_component_summary(self.firstOrderVolterra.value)


@xai_component(color='rgb(253, 225, 0)')
class MixtureOfGammas(Component):
    from tvb.datatypes.equations import MixtureOfGammas
    parameters: InArg[dict]

    mixtureOfGammas: OutArg[Equation]

    def __init__(self):
        set_defaults(self, self.MixtureOfGammas)

    def execute(self, ctx) -> None:
        mixtureOfGammas = self.MixtureOfGammas()

        set_values(self, mixtureOfGammas)
        self.mixtureOfGammas.value = mixtureOfGammas
        print_component_summary(self.mixtureOfGammas.value)

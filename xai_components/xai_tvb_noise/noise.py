# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import numpy
from tvb.simulator.noise import Noise
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class Additive(TVBComponent):
    """Xircuits component for configuring additive noise in TVB simulations.

    Additive noise introduces random fluctuations to the simulation state
    variables that are independent of the current system state. This is
    the most common noise type used in stochastic brain simulations.

    Inputs:
        ntau: Noise correlation time constant. Controls the temporal
              smoothness of the noise signal.
        noise_seed: Seed for the random number generator, enabling
                    reproducible noise across simulation runs.
        random_stream: NumPy RandomState object for generating the
                       random noise values.
        nsig: Noise amplitude (standard deviation). Can be a single
              float for uniform noise or a numpy array for different
              noise levels per state variable.

    Output:
        additive: Configured TVB Additive noise instance ready to be
                  connected to an integrator component.
    """
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[numpy.random.RandomState]
    nsig: InArg[Union[float, numpy.ndarray]]

    additive: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.noise import Additive
        return Additive

    def execute(self, ctx) -> None:
        additive = self.tvb_ht_class()

        set_values(self, additive)
        self.additive.value = additive
        print_component_summary(self.additive.value)


@xai_component(color='rgb(253, 225, 0)')
class Multiplicative(TVBComponent):
    """Xircuits component for configuring multiplicative noise in TVB simulations.

    Multiplicative noise produces state-dependent random fluctuations where
    the noise amplitude is modulated by a temporal equation applied to the
    current system state. This creates more realistic noise patterns where
    the variability scales with neural activity.

    Inputs:
        ntau: Noise correlation time constant. Controls the temporal
              smoothness of the noise signal.
        noise_seed: Seed for the random number generator, enabling
                    reproducible noise across simulation runs.
        random_stream: NumPy RandomState object for generating the
                       random noise values.
        nsig: Noise amplitude (standard deviation). Can be a single
              float or a numpy array for per-variable noise levels.
        b: Temporal equation that governs how the noise amplitude
           depends on the current state of the system.

    Output:
        multiplicative: Configured TVB Multiplicative noise instance
                        ready to be connected to an integrator component.
    """
    from tvb.datatypes.equations import TemporalApplicableEquation
    ntau: InArg[float]
    noise_seed: InArg[int]
    random_stream: InArg[numpy.random.RandomState]
    nsig: InArg[Union[float, numpy.ndarray]]
    b: InArg[TemporalApplicableEquation]

    multiplicative: OutArg[Noise]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.noise import Multiplicative
        return Multiplicative

    def execute(self, ctx) -> None:
        multiplicative = self.tvb_ht_class()

        set_values(self, multiplicative)
        self.multiplicative.value = multiplicative
        print_component_summary(self.multiplicative.value)
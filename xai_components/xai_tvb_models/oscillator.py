# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import numpy
from tvb.simulator.models.base import Model
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class Generic2dOscillator(ComponentWithWidget):
    """Xircuits component for the Generic 2D Oscillator neural mass model.

    A two-dimensional oscillator model that can reproduce the dynamics of
    several well-known neural models depending on the parameter configuration.
    It is commonly used for simulating basic neural population dynamics in TVB.

    Inputs:
        tau: Time scale of the model dynamics.
        I: External input current driving the system.
        a: Model parameter controlling the shape of the nullcline.
        b: Model parameter affecting the fast variable dynamics.
        c: Model parameter for the slow variable influence.
        d: Time scale ratio between fast and slow variables.
        e: Coefficient for the quadratic term.
        f: Coefficient for the cubic term.
        g: Coefficient for the linear coupling term.
        alpha: Scaling parameter for the fast variable.
        beta: Scaling parameter for the slow variable.
        gamma: Additional scaling parameter.
        variables_of_interest: List of state variables to record during simulation.

    Output:
        generic2dOscillator: Configured TVB Generic2dOscillator model instance.
    """
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
    """Xircuits component for the Kuramoto coupled oscillator model.

    The Kuramoto model describes the synchronization behavior of coupled
    oscillators. Each oscillator has a natural frequency and tends to
    synchronize with its neighbors through coupling.

    Inputs:
        omega: Natural frequency of the oscillators.
        variables_of_interest: List of state variables to record during simulation.

    Output:
        kuramoto: Configured TVB Kuramoto model instance.
    """
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
    """Xircuits component for the Supercritical Hopf bifurcation model.

    The Supercritical Hopf model describes the transition from a stable
    fixed point to a limit cycle oscillation. It is used to model the
    onset of neural oscillations in brain regions.

    Inputs:
        a: Bifurcation parameter controlling the transition between
           stable and oscillatory states. Negative values produce a
           stable fixed point, positive values produce oscillations.
        omega: Natural frequency of the oscillations.
        variables_of_interest: List of state variables to record during simulation.

    Output:
        supHopf: Configured TVB SupHopf model instance.
    """
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
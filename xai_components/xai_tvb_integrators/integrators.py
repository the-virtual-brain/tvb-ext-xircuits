# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.integrators import Integrator
from tvb.simulator.noise import Noise

from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class HeunDeterministic(Component):
    from tvb.simulator.integrators import HeunDeterministic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    heunDeterministic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.HeunDeterministic)

    def execute(self, ctx) -> None:
        heunDeterministic = self.HeunDeterministic()

        set_values(self, heunDeterministic)
        self.heunDeterministic.value = heunDeterministic
        print_component_summary(self.heunDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class HeunStochastic(Component):
    from tvb.simulator.integrators import HeunStochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    heunStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.HeunStochastic)

    def execute(self, ctx) -> None:
        heunStochastic = self.HeunStochastic()

        set_values(self, heunStochastic)
        self.heunStochastic.value = heunStochastic
        print_component_summary(self.heunStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class EulerDeterministic(Component):
    from tvb.simulator.integrators import EulerDeterministic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    eulerDeterministic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.EulerDeterministic)

    def execute(self, ctx) -> None:
        eulerDeterministic = self.EulerDeterministic()

        set_values(self, eulerDeterministic)
        self.eulerDeterministic.value = eulerDeterministic
        print_component_summary(self.eulerDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class EulerStochastic(Component):
    from tvb.simulator.integrators import EulerStochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    eulerStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.EulerStochastic)

    def execute(self, ctx) -> None:
        eulerStochastic = self.EulerStochastic()

        set_values(self, eulerStochastic)
        self.eulerStochastic.value = eulerStochastic
        print_component_summary(self.eulerStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class RungeKutta4thOrderDeterministic(Component):
    from tvb.simulator.integrators import RungeKutta4thOrderDeterministic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    rungeKutta4thOrderDeterministic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.RungeKutta4thOrderDeterministic)

    def execute(self, ctx) -> None:
        rungeKutta4thOrderDeterministic = self.RungeKutta4thOrderDeterministic()

        set_values(self, rungeKutta4thOrderDeterministic)
        self.rungeKutta4thOrderDeterministic.value = rungeKutta4thOrderDeterministic
        print_component_summary(self.rungeKutta4thOrderDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class Identity(Component):
    from tvb.simulator.integrators import Identity
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    identity: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.Identity)

    def execute(self, ctx) -> None:
        identity = self.Identity()

        set_values(self, identity)
        self.identity.value = identity
        print_component_summary(self.identity.value)


@xai_component(color='rgb(253, 225, 0)')
class IdentityStochastic(Component):
    from tvb.simulator.integrators import IdentityStochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    identityStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.IdentityStochastic)

    def execute(self, ctx) -> None:
        identityStochastic = self.IdentityStochastic()

        set_values(self, identityStochastic)
        self.identityStochastic.value = identityStochastic
        print_component_summary(self.identityStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class VODE(Component):
    from tvb.simulator.integrators import VODE
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    vODE: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.VODE)

    def execute(self, ctx) -> None:
        vODE = self.VODE()

        set_values(self, vODE)
        self.vODE.value = vODE
        print_component_summary(self.vODE.value)


@xai_component(color='rgb(253, 225, 0)')
class VODEStochastic(Component):
    from tvb.simulator.integrators import VODEStochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    vODEStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.VODEStochastic)

    def execute(self, ctx) -> None:
        vODEStochastic = self.VODEStochastic()

        set_values(self, vODEStochastic)
        self.vODEStochastic.value = vODEStochastic
        print_component_summary(self.vODEStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class Dopri5(Component):
    from tvb.simulator.integrators import Dopri5
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    dopri5: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.Dopri5)

    def execute(self, ctx) -> None:
        dopri5 = self.Dopri5()

        set_values(self, dopri5)
        self.dopri5.value = dopri5
        print_component_summary(self.dopri5.value)


@xai_component(color='rgb(253, 225, 0)')
class Dopri5Stochastic(Component):
    from tvb.simulator.integrators import Dopri5Stochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    dopri5Stochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.Dopri5Stochastic)

    def execute(self, ctx) -> None:
        dopri5Stochastic = self.Dopri5Stochastic()

        set_values(self, dopri5Stochastic)
        self.dopri5Stochastic.value = dopri5Stochastic
        print_component_summary(self.dopri5Stochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class Dop853(Component):
    from tvb.simulator.integrators import Dop853
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    dop853: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.Dop853)

    def execute(self, ctx) -> None:
        dop853 = self.Dop853()

        set_values(self, dop853)
        self.dop853.value = dop853
        print_component_summary(self.dop853.value)


@xai_component(color='rgb(253, 225, 0)')
class Dop853Stochastic(Component):
    from tvb.simulator.integrators import Dop853Stochastic
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    dop853Stochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.Dop853Stochastic)

    def execute(self, ctx) -> None:
        dop853Stochastic = self.Dop853Stochastic()

        set_values(self, dop853Stochastic)
        self.dop853Stochastic.value = dop853Stochastic
        print_component_summary(self.dop853Stochastic.value)
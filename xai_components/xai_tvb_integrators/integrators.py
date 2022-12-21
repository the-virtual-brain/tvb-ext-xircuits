# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.integrators import Integrator
from tvb.simulator.noise import Noise

from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(253, 225, 0)')
class HeunDeterministic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    heunDeterministic: OutArg[Integrator]


    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import HeunDeterministic
        return HeunDeterministic

    def execute(self, ctx) -> None:
        heunDeterministic = self.tvb_ht_class()

        set_values(self, heunDeterministic)
        self.heunDeterministic.value = heunDeterministic
        print_component_summary(self.heunDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class HeunStochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    heunStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import HeunStochastic
        return HeunStochastic

    def execute(self, ctx) -> None:
        heunStochastic = self.tvb_ht_class()

        set_values(self, heunStochastic)
        self.heunStochastic.value = heunStochastic
        print_component_summary(self.heunStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class EulerDeterministic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    eulerDeterministic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import EulerDeterministic
        return EulerDeterministic

    def execute(self, ctx) -> None:
        eulerDeterministic = self.tvb_ht_class()

        set_values(self, eulerDeterministic)
        self.eulerDeterministic.value = eulerDeterministic
        print_component_summary(self.eulerDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class EulerStochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    eulerStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import EulerStochastic
        return EulerStochastic

    def execute(self, ctx) -> None:
        eulerStochastic = self.tvb_ht_class()

        set_values(self, eulerStochastic)
        self.eulerStochastic.value = eulerStochastic
        print_component_summary(self.eulerStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class RungeKutta4thOrderDeterministic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    rungeKutta4thOrderDeterministic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import RungeKutta4thOrderDeterministic
        return RungeKutta4thOrderDeterministic


    def execute(self, ctx) -> None:
        rungeKutta4thOrderDeterministic = self.tvb_ht_class()

        set_values(self, rungeKutta4thOrderDeterministic)
        self.rungeKutta4thOrderDeterministic.value = rungeKutta4thOrderDeterministic
        print_component_summary(self.rungeKutta4thOrderDeterministic.value)


@xai_component(color='rgb(253, 225, 0)')
class Identity(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    identity: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import Identity
        return Identity

    def execute(self, ctx) -> None:
        identity = self.tvb_ht_class()

        set_values(self, identity)
        self.identity.value = identity
        print_component_summary(self.identity.value)


@xai_component(color='rgb(253, 225, 0)')
class IdentityStochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    identityStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import IdentityStochastic
        return IdentityStochastic

    def execute(self, ctx) -> None:
        identityStochastic = self.tvb_ht_class()

        set_values(self, identityStochastic)
        self.identityStochastic.value = identityStochastic
        print_component_summary(self.identityStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class VODE(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    vODE: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import VODE
        return VODE

    def execute(self, ctx) -> None:
        vODE = self.tvb_ht_class()

        set_values(self, vODE)
        self.vODE.value = vODE
        print_component_summary(self.vODE.value)


@xai_component(color='rgb(253, 225, 0)')
class VODEStochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    vODEStochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import VODEStochastic
        return VODEStochastic

    def execute(self, ctx) -> None:
        vODEStochastic = self.tvb_ht_class()

        set_values(self, vODEStochastic)
        self.vODEStochastic.value = vODEStochastic
        print_component_summary(self.vODEStochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class Dopri5(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    dopri5: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import Dopri5
        return Dopri5

    def execute(self, ctx) -> None:
        dopri5 = self.tvb_ht_class()

        set_values(self, dopri5)
        self.dopri5.value = dopri5
        print_component_summary(self.dopri5.value)


@xai_component(color='rgb(253, 225, 0)')
class Dopri5Stochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    dopri5Stochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import Dopri5Stochastic
        return Dopri5Stochastic

    def execute(self, ctx) -> None:
        dopri5Stochastic = self.tvb_ht_class()

        set_values(self, dopri5Stochastic)
        self.dopri5Stochastic.value = dopri5Stochastic
        print_component_summary(self.dopri5Stochastic.value)


@xai_component(color='rgb(253, 225, 0)')
class Dop853(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]

    dop853: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import Dop853
        return Dop853

    def execute(self, ctx) -> None:
        dop853 = self.tvb_ht_class()

        set_values(self, dop853)
        self.dop853.value = dop853
        print_component_summary(self.dop853.value)


@xai_component(color='rgb(253, 225, 0)')
class Dop853Stochastic(TVBComponent):
    dt: InArg[float]
    bounded_state_variable_indices: InArg[list]
    state_variable_boundaries: InArg[list]
    clamped_state_variable_indices: InArg[list]
    clamped_state_variable_values: InArg[list]
    noise: InArg[Noise]

    dop853Stochastic: OutArg[Integrator]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.integrators import Dop853Stochastic
        return Dop853Stochastic

    def execute(self, ctx) -> None:
        dop853Stochastic = self.tvb_ht_class()

        set_values(self, dop853Stochastic)
        self.dop853Stochastic.value = dop853Stochastic
        print_component_summary(self.dop853Stochastic.value)
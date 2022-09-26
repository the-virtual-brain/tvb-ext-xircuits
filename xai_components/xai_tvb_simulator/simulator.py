# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.connectivity import Connectivity
from tvb.datatypes.cortex import Cortex
from tvb.datatypes.patterns import SpatioTemporalPattern
from tvb.simulator.coupling import Coupling
from tvb.simulator.integrators import Integrator
from tvb.simulator.models.base import Model

from xai_components.base import InArg, OutArg, Component, xai_component
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(220, 5, 45)')
class Simulator(Component):
    from tvb.simulator.simulator import Simulator
    connectivity: InArg[Connectivity]
    conduction_speed: InArg[float]
    coupling: InArg[Coupling]
    surface: InArg[Cortex]
    stimulus: InArg[SpatioTemporalPattern]
    model: InArg[Model]
    integrator: InArg[Integrator]
    initial_conditions: InArg[list]
    monitors: InArg[list]
    simulation_length: InArg[float]

    simulator: OutArg[Simulator]

    def __init__(self):
        set_defaults(self, self.Simulator)

    def execute(self, ctx) -> None:
        simulator = self.Simulator()
        set_values(self, simulator)
        simulator.configure()

        self.simulator.value = simulator
        print_component_summary(self.simulator.value)
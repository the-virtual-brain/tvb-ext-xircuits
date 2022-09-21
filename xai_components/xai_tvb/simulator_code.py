# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy as np
from tvb.datatypes.connectivity import Connectivity
from tvb.simulator.coupling import Coupling
from tvb.simulator.integrators import HeunDeterministic
from tvb.simulator.models.oscillator import Generic2dOscillator
from tvb.simulator.simulator import Simulator

from xai_components.base import InArg, OutArg, Component, xai_component
from xai_components.xai_tvb.utils import print_component_summary


@xai_component
class ConnectivityComponent(Component):
    connectivity: OutArg[Connectivity]

    def __init__(self):
        self.done = False

        self.connectivity = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from matplotlib import pyplot as plt
        from tvb.simulator.lab import connectivity

        self.connectivity.value = connectivity.Connectivity.from_file('connectivity_66.zip')
        print_component_summary(self.connectivity.value)

        plt.imshow(self.connectivity.value.weights, interpolation='none')
        plt.show()


@xai_component
class LinearCouplingComponent(Component):
    float_a: InArg[float]
    float_b: InArg[float]

    linear_coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False

        self.float_a = InArg(None)
        self.float_b = InArg(None)
        self.linear_coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.lab import coupling

        a = self.float_a.value
        b = self.float_b.value
        if not b:
            b = 0.0

        linear_coupling = coupling.Linear(a=np.array([a]), b=np.array([b]))
        self.linear_coupling.value = linear_coupling
        print_component_summary(self.linear_coupling.value)


class ComponentWithWidget(Component):
    """
    Used to flag a component that has an associate widget to be displayed in Xircuits UI for interactive setup.
    """


@xai_component
class Generic2dOscillatorComponent(ComponentWithWidget):
    model: OutArg[Generic2dOscillator]

    def __init__(self):
        self.done = False

        self.model = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.lab import models

        model = models.Generic2dOscillator()
        self.model.value = model
        print_component_summary(self.model.value)


@xai_component
class HeunDeterministicComponent(Component):
    integrator: OutArg[HeunDeterministic]

    def __init__(self):
        self.done = False

        self.integrator = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.lab import integrators

        integrator = integrators.HeunDeterministic()
        self.integrator.value = integrator
        print_component_summary(self.integrator.value)


@xai_component
class MonitorsComponent(Component):
    monitors: OutArg[list]

    def __init__(self):
        self.done = False

        self.monitors = OutArg.empty()

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.lab import monitors

        monitors_list = []
        temporal_average = monitors.TemporalAverage()
        print_component_summary(temporal_average)

        monitors_list.append(temporal_average)
        self.monitors.value = monitors_list


@xai_component
class SimulatorComponent(Component):
    connectivity: InArg[Connectivity]
    coupling: InArg[Coupling]
    model: InArg[Generic2dOscillator]
    integrator: InArg[HeunDeterministic]
    monitors: InArg[list]
    simulation_length: InArg[float]

    simulator: OutArg[Simulator]

    def __init__(self):
        self.done = False

        self.connectivity = InArg(None)
        self.coupling = InArg(None)
        self.model = InArg(None)
        self.integrator = InArg(None)
        self.monitors = InArg(None)
        self.simulation_length = InArg(None)
        self.simulator = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator import simulator
        sim = simulator.Simulator(
            connectivity=self.connectivity.value,
            coupling=self.coupling.value,
            model=self.model.value,
            integrator=self.integrator.value,
            monitors=self.monitors.value,
            simulation_length=self.simulation_length.value
        ).configure()

        self.simulator.value = sim
        print_component_summary(self.simulator.value)
        self.done = True

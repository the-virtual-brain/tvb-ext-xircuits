# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from tvb.datatypes.time_series import TimeSeries
from tvb.simulator.backend.templates import MakoUtilMix
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
    backend: InArg[MakoUtilMix]

    time_series: OutArg[TimeSeries]

    def __init__(self):
        set_defaults(self, self.Simulator)
        self.backend = InArg(None)
        self.time_series = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.backend.nb_mpr import NbMPRBackend
        from tvb.datatypes import time_series

        simulator = self.Simulator()
        set_values(self, simulator)
        simulator.configure()

        print_component_summary(simulator)

        # run simulation
        backend = self.backend.value
        if isinstance(backend, NbMPRBackend):
            (time, data), = backend.run_sim(simulator, simulation_length=simulator.simulation_length)
        else:
            (time, data), = simulator.run()

        # create TS
        tsr = time_series.TimeSeriesRegion(
            data=data,
            time=time,
            connectivity=simulator.connectivity,
            sample_period=simulator.monitors[0].period / 1e3,
            sample_period_unit='s')
        tsr.configure()
        print_component_summary(tsr)


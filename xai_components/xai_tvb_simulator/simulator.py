# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from tvb.simulator.backend.templates import MakoUtilMix
from tvb.datatypes.connectivity import Connectivity
from tvb.datatypes.cortex import Cortex
from tvb.datatypes.patterns import SpatioTemporalPattern
from tvb.simulator.coupling import Coupling
from tvb.simulator.integrators import Integrator
from tvb.simulator.models.base import Model

from xai_components.base import InArg, OutArg, xai_component, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(220, 5, 45)')
class Simulator(TVBComponent):
    connectivity: InCompArg[Connectivity]
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

    time_series_list: OutArg[list]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)
        self.backend = InArg(None)
        self.time_series = OutArg(None)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.simulator import Simulator
        return Simulator

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.backend.nb_mpr import NbMPRBackend

        simulator = self.tvb_ht_class()
        set_values(self, simulator)
        simulator.configure()

        print_component_summary(simulator)

        # run simulation
        backend = self.backend.value
        if isinstance(backend, NbMPRBackend):
            result = backend.run_sim(simulator, simulation_length=simulator.simulation_length)
        else:
            result = simulator.run()

        # create TS
        ts_list = []
        for i in range(len(simulator.monitors)):
            monitor = simulator.monitors[i]
            time, data = result[i]
            ts = monitor.create_time_series(connectivity=simulator.connectivity)
            ts.data = data
            ts.time = time
            ts.configure()
            ts_list.append(ts)

        for ts in ts_list:
            print_component_summary(ts)


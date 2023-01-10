# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
import datetime
import os.path

import numpy
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
    output_directory: InArg[str]

    time_series_list: OutArg[list]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)
        self.backend = InArg(None)
        self.time_series = OutArg(None)
        self.output_directory = InArg("results")

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

        # prepare output folder
        if os.path.isdir(self.output_directory.value):
            self.output_directory.value += f"_{datetime.datetime.now().strftime('%m.%d.%Y_%H:%M:%S')}"
        os.mkdir(self.output_directory.value)

        # create TS
        ts_list = []
        for i in range(len(simulator.monitors)):
            monitor = simulator.monitors[i]
            time, data = result[i]
            ts = monitor.create_time_series(connectivity=simulator.connectivity)
            ts.data = data
            ts.time = time
            ts.configure()

            monitor_name = type(monitor).__name__
            ts_file_name = os.path.join(self.output_directory.value, f"timeseries_{monitor_name}.npy")
            print(f"Storing timeseries for {monitor_name} monitor to {ts_file_name}...")
            numpy.save(ts_file_name, ts.data)

            print_component_summary(ts)
            ts_list.append(ts)


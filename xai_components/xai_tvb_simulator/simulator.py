# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#
import time

from tvb.datatypes.connectivity import Connectivity
from tvb.datatypes.cortex import Cortex
from tvb.datatypes.patterns import SpatioTemporalPattern
from tvb.simulator.coupling import Coupling
from tvb.simulator.integrators import Integrator
from tvb.simulator.models.base import Model

from xai_components.base import InArg, OutArg, xai_component, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values
from xai_components.logger.builder import get_logger

LOGGER = get_logger(__name__)


@xai_component(color='rgb(220, 5, 45)')
class Simulator(TVBComponent):
    """Xircuits component for running TVB brain network simulations.

    This is the central simulation component that brings together all the
    pieces needed for a full brain simulation: connectivity, neural mass
    model, coupling function, integrator, and monitors. It configures
    a TVB Simulator, runs the simulation, and produces time series output
    for each monitor.

    Inputs:
        connectivity: Brain connectivity matrix defining the structural
                      connections between brain regions (weights and tract lengths).
        conduction_speed: Speed of signal propagation between regions in mm/ms.
        coupling: Coupling function defining how connected regions influence
                  each other during simulation.
        surface: Optional cortical surface mesh for surface-based simulations.
        stimulus: Optional spatiotemporal stimulation pattern applied during
                  the simulation.
        model: Neural mass model describing the local dynamics at each
               brain region (e.g., Generic2dOscillator, Epileptor).
        integrator: Numerical integration scheme used to solve the model
                    equations (e.g., HeunDeterministic, EulerStochastic).
        initial_conditions: Optional initial state values for the simulation.
        monitors: List of monitors that define what data to record and at
                  what sampling rate (e.g., TemporalAverage, Raw).
        simulation_length: Total duration of the simulation in milliseconds.

    Output:
        time_series_list: List of TimeSeries objects, one for each monitor,
                          containing the recorded simulation data.
    """
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

    time_series_list: OutArg[list]

    def __init__(self):
        set_defaults(self, self.tvb_ht_class)
        self.time_series_list = OutArg(None)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.simulator import Simulator
        return Simulator

    def execute(self, ctx) -> None:
        # validate required inputs
        if self.connectivity.value is None:
            raise ValueError(
                "Connectivity is required to run a simulation. "
                "Please connect a ConnectivityFromFile component."
            )

        simulator = self.tvb_ht_class()
        set_values(self, simulator)

        try:
            simulator.configure()
        except Exception as e:
            LOGGER.error(f"Simulator configuration failed: {e}")
            raise ValueError(
                f"Failed to configure the simulator. Please check that "
                f"all required inputs are properly connected. Error: {e}"
            ) from e

        print_component_summary(simulator)

        # run simulation with timing
        LOGGER.info("Starting simulation...")
        start_time = time.time()

        try:
            result = simulator.run()
        except Exception as e:
            LOGGER.error(f"Simulation failed: {e}")
            raise RuntimeError(
                f"Simulation failed during execution. Error: {e}"
            ) from e

        elapsed = time.time() - start_time
        LOGGER.info(f"Simulation completed in {elapsed:.2f} seconds.")

        # create TS
        self.time_series_list.value = []
        for i in range(len(simulator.monitors)):
            monitor = simulator.monitors[i]
            time_data, data = result[i]
            ts = monitor.create_time_series(connectivity=simulator.connectivity)
            ts.data = data
            ts.time = time_data
            ts.title = type(monitor).__name__
            ts.configure()

            print_component_summary(ts)
            self.time_series_list.value.append(ts)

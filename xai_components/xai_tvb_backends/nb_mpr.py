# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
import numpy as np
from tvb.simulator.simulator import Simulator

from xai_components.base import xai_component, InArg, OutArg, Component


@xai_component(color='rgb(101, 179, 46)')
class NbMPRBackend(Component):
    simulator: InArg[Simulator]
    time: OutArg[np.ndarray]
    data: OutArg[np.ndarray]

    def __init__(self):
        self.done = False

        self.simulator = InArg(None)
        self.time = OutArg(None)
        self.date = OutArg(None)

    def execute(self, ctx) -> None:
        from tvb.simulator.backend.nb_mpr import NbMPRBackend
        nbMPRBackend = NbMPRBackend()
        sim = self.simulator.value
        (time, data), = nbMPRBackend.run_sim(sim=sim, simulation_length=sim.simulation_length)
        print(time.shape)
        print(data.shape)

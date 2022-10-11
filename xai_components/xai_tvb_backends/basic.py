# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
import numpy as np
from tvb.simulator.simulator import Simulator

from xai_components.base import xai_component, InArg, OutArg, Component


@xai_component(color='rgb(101, 179, 46)')
class BasicBackend(Component):
    simulator: InArg[Simulator]
    time: OutArg[np.ndarray]
    data: OutArg[np.ndarray]

    def __init__(self):
        self.done = False

        self.simulator = InArg(None)
        self.time = OutArg(None)
        self.date = OutArg(None)

    def execute(self, ctx) -> None:
        (time, data), = self.simulator.value.run()
        print(time.shape)
        print(data.shape)
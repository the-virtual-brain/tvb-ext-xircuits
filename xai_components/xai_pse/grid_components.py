# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import itertools
from xai_components.base import Component, InArg, OutArg, xai_component


@xai_component(color='rgb(92, 107, 192)')
class PSEParameterGrid(Component):
    param1_values: InArg[list]
    param2_values: InArg[list]
    param1_name: InArg[str]
    param2_name: InArg[str]
    grid_combinations: OutArg[list]
    param1_axis: OutArg[list]
    param2_axis: OutArg[list]
    grid_shape: OutArg[tuple]
    total_simulations: OutArg[int]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.param1_values = InArg(None)
        self.param2_values = InArg(None)
        self.param1_name = InArg("param1")
        self.param2_name = InArg("param2")
        self.grid_combinations = OutArg(None)
        self.param1_axis = OutArg(None)
        self.param2_axis = OutArg(None)
        self.grid_shape = OutArg(None)
        self.total_simulations = OutArg(None)

    def execute(self, ctx) -> None:
        p1 = self.param1_values.value
        p2 = self.param2_values.value

        if p1 is None or len(p1) == 0:
            raise ValueError(
                "PSEParameterGrid: param1_values is empty or not connected. "
                "Connect a PSELinspaceRange or PSEValueList component."
            )
        if p2 is None or len(p2) == 0:
            raise ValueError(
                "PSEParameterGrid: param2_values is empty or not connected. "
                "Connect a PSELinspaceRange or PSEValueList component."
            )

        p1_name = self.param1_name.value or "param1"
        p2_name = self.param2_name.value or "param2"

        combinations = list(itertools.product(p1, p2))

        self.grid_combinations.value = combinations
        self.param1_axis.value = list(p1)
        self.param2_axis.value = list(p2)
        self.grid_shape.value = (len(p1), len(p2))
        self.total_simulations.value = len(combinations)

        ctx["pse_param1_name"] = p1_name
        ctx["pse_param2_name"] = p2_name
        ctx["pse_param1_axis"] = list(p1)
        ctx["pse_param2_axis"] = list(p2)
        ctx["pse_grid_shape"] = (len(p1), len(p2))

        print(f"[PSEParameterGrid] Created {len(p1)}x{len(p2)} = "
              f"{len(combinations)} combinations")
        print(f"  {p1_name}: {p1[0]:.4f} -> {p1[-1]:.4f} ({len(p1)} points)")
        print(f"  {p2_name}: {p2[0]:.4f} -> {p2[-1]:.4f} ({len(p2)} points)")

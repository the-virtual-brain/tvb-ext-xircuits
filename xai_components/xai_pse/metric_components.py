# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import numpy
from xai_components.base import Component, InArg, OutArg, xai_component


@xai_component(color='rgb(38, 166, 154)')
class PSEResultCollector(Component):
    single_result: InArg[any]
    accumulated: InArg[list]
    accumulated_out: OutArg[list]
    count: OutArg[int]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.single_result = InArg(None)
        self.accumulated = InArg(None)
        self.accumulated_out = OutArg(None)
        self.count = OutArg(None)

    def execute(self, ctx) -> None:
        current_list = self.accumulated.value if self.accumulated.value is not None else []

        new_result = self.single_result.value
        if new_result is None:
            raise ValueError(
                "PSEResultCollector: single_result is None. "
                "Ensure the Simulator component output is connected."
            )

        current_list.append(new_result)
        self.accumulated_out.value = current_list
        self.count.value = len(current_list)
        print(f"[PSEResultCollector] Collected result #{len(current_list)}")


@xai_component(color='rgb(38, 166, 154)')
class PSEGlobalVariance(Component):
    simulation_results: InArg[list]
    grid_shape: InArg[tuple]
    metric_values: OutArg[list]
    metric_matrix: OutArg[any]
    metric_name: OutArg[str]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.simulation_results = InArg(None)
        self.grid_shape = InArg(None)
        self.metric_values = OutArg(None)
        self.metric_matrix = OutArg(None)
        self.metric_name = OutArg(None)

    def execute(self, ctx) -> None:
        results = self.simulation_results.value
        if results is None or len(results) == 0:
            raise ValueError(
                "PSEGlobalVariance: no simulation results provided. "
                "Connect PSEResultCollector accumulated_out."
            )

        variances = []
        for i, result in enumerate(results):
            try:
                ts = numpy.array(result) if not isinstance(result, numpy.ndarray) else result
                variance = float(numpy.var(ts))
                variances.append(variance)
            except Exception as e:
                print(f"[PSEGlobalVariance] Warning: could not compute "
                      f"variance for result #{i}: {e}")
                variances.append(float('nan'))

        self.metric_values.value = variances
        self.metric_name.value = "Global Variance"

        shape = self.grid_shape.value
        if shape is not None and len(shape) == 2:
            expected = shape[0] * shape[1]
            if len(variances) == expected:
                self.metric_matrix.value = numpy.array(variances).reshape(shape)
                print(f"[PSEGlobalVariance] Computed {shape[0]}x{shape[1]} "
                      f"variance matrix")
            else:
                print(f"[PSEGlobalVariance] Warning: expected {expected} "
                      f"results but got {len(variances)}, skipping reshape")
                self.metric_matrix.value = numpy.array(variances)
        else:
            self.metric_matrix.value = numpy.array(variances)

        print(f"[PSEGlobalVariance] Range: "
              f"[{numpy.nanmin(variances):.6f}, {numpy.nanmax(variances):.6f}]")


@xai_component(color='rgb(38, 166, 154)')
class PSEVarianceOfVariance(Component):
    simulation_results: InArg[list]
    grid_shape: InArg[tuple]
    metric_values: OutArg[list]
    metric_matrix: OutArg[any]
    metric_name: OutArg[str]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.simulation_results = InArg(None)
        self.grid_shape = InArg(None)
        self.metric_values = OutArg(None)
        self.metric_matrix = OutArg(None)
        self.metric_name = OutArg(None)

    def execute(self, ctx) -> None:
        results = self.simulation_results.value
        if results is None or len(results) == 0:
            raise ValueError(
                "PSEVarianceOfVariance: no simulation results provided."
            )

        vov_values = []
        for i, result in enumerate(results):
            try:
                ts = numpy.array(result) if not isinstance(result, numpy.ndarray) else result
                if ts.ndim >= 3:
                    var_per_region = numpy.var(ts, axis=0)
                    vov = float(numpy.var(var_per_region))
                else:
                    vov = float(numpy.var(numpy.var(ts, axis=0)))
                vov_values.append(vov)
            except Exception as e:
                print(f"[PSEVarianceOfVariance] Warning: result #{i}: {e}")
                vov_values.append(float('nan'))

        self.metric_values.value = vov_values
        self.metric_name.value = "Variance of Variance"

        shape = self.grid_shape.value
        if shape and len(shape) == 2 and len(vov_values) == shape[0] * shape[1]:
            self.metric_matrix.value = numpy.array(vov_values).reshape(shape)
        else:
            self.metric_matrix.value = numpy.array(vov_values)

        print(f"[PSEVarianceOfVariance] Computed for {len(vov_values)} simulations")

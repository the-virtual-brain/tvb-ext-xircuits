# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import numpy
from xai_components.base import Component, InArg, OutArg, xai_component


@xai_component(color='rgb(126, 87, 194)')
class PSELinspaceRange(Component):
    start: InArg[float]
    stop: InArg[float]
    num_points: InArg[int]
    values: OutArg[list]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.start = InArg(0.0)
        self.stop = InArg(1.0)
        self.num_points = InArg(10)
        self.values = OutArg(None)

    def execute(self, ctx) -> None:
        start_val = self.start.value if self.start.value is not None else 0.0
        stop_val = self.stop.value if self.stop.value is not None else 1.0
        n_points = self.num_points.value if self.num_points.value is not None else 10

        if n_points < 1:
            raise ValueError(
                f"PSELinspaceRange: num_points must be >= 1, got {n_points}"
            )
        if start_val >= stop_val:
            raise ValueError(
                f"PSELinspaceRange: start ({start_val}) must be < stop ({stop_val})"
            )

        result = numpy.linspace(start_val, stop_val, n_points).tolist()
        self.values.value = result
        print(f"[PSELinspaceRange] Generated {len(result)} values: "
              f"[{result[0]:.4f} ... {result[-1]:.4f}]")


@xai_component(color='rgb(126, 87, 194)')
class PSEArangeRange(Component):
    start: InArg[float]
    stop: InArg[float]
    step: InArg[float]
    values: OutArg[list]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.start = InArg(0.0)
        self.stop = InArg(1.0)
        self.step = InArg(0.1)
        self.values = OutArg(None)

    def execute(self, ctx) -> None:
        start_val = self.start.value if self.start.value is not None else 0.0
        stop_val = self.stop.value if self.stop.value is not None else 1.0
        step_val = self.step.value if self.step.value is not None else 0.1

        if step_val <= 0:
            raise ValueError(
                f"PSEArangeRange: step must be > 0, got {step_val}"
            )
        if start_val >= stop_val:
            raise ValueError(
                f"PSEArangeRange: start ({start_val}) must be < stop ({stop_val})"
            )

        result = numpy.arange(start_val, stop_val, step_val).tolist()
        self.values.value = result
        print(f"[PSEArangeRange] Generated {len(result)} values "
              f"with step {step_val}")


@xai_component(color='rgb(126, 87, 194)')
class PSEValueList(Component):
    values_string: InArg[str]
    values: OutArg[list]

    def __init__(self):
        self.__id__ = None
        self.next = None
        self.done = False
        self.values_string = InArg(None)
        self.values = OutArg(None)

    def execute(self, ctx) -> None:
        raw = self.values_string.value
        if raw is None or raw.strip() == "":
            raise ValueError(
                "PSEValueList: values_string cannot be empty. "
                "Provide comma-separated floats, e.g. '0.1, 0.5, 1.0'"
            )

        try:
            result = [float(v.strip()) for v in raw.split(",")]
        except ValueError as e:
            raise ValueError(
                f"PSEValueList: could not parse '{raw}' as comma-separated "
                f"floats. Error: {e}"
            )

        if len(result) == 0:
            raise ValueError("PSEValueList: parsed an empty list")

        self.values.value = result
        print(f"[PSEValueList] Loaded {len(result)} custom values: {result}")

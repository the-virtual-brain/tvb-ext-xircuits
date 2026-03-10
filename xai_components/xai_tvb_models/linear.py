# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2025, TVB Widgets Team
#

import numpy
from tvb.simulator.models.base import Model
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class LinearModel(ComponentWithWidget):
    """Xircuits component for the Linear neural mass model.

    A simple linear model where the dynamics follow a first-order linear
    differential equation. Useful for testing simulation pipelines and
    as a baseline model for comparison with more complex neural models.

    Inputs:
        gamma: Rate constant controlling the decay of the linear model.
               Determines how quickly the state variable returns to equilibrium.
        variables_of_interest: List of state variables to record during simulation.
        parameter_names: List of parameter names used by the model.

    Output:
        linear: Configured TVB Linear model instance.
    """
    gamma: InArg[Union[float, numpy.ndarray]]
    variables_of_interest: InArg[list]
    parameter_names: InArg[list]

    linear: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.linear import Linear
        return Linear

    def execute(self, ctx) -> None:
        linear = self.tvb_ht_class()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)
# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(101, 179, 46)')
class Linear(Component):
    from tvb.simulator.models.linear import Linear
    gamma: InArg[list]
    variables_of_interest: InArg[list]
    parameter_names: InArg[list]

    linear: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Linear)

    def execute(self, ctx) -> None:
        linear = self.Linear()

        set_values(self, linear)
        self.linear.value = linear
        print_component_summary(self.linear.value)
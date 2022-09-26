# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class LinearModel(ComponentWithWidget):
    gamma: InArg[float]
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

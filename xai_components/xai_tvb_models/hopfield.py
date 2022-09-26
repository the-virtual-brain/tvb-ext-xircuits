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
class Hopfield(Component):
    from tvb.simulator.models.hopfield import Hopfield
    taux: InArg[float]
    tauT: InArg[float]
    dynamic: InArg[int]
    variables_of_interest: InArg[list]

    hopfield: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.Hopfield)

    def execute(self, ctx) -> None:
        hopfield = self.Hopfield()

        set_values(self, hopfield)
        self.hopfield.value = hopfield
        print_component_summary(self.hopfield.value)
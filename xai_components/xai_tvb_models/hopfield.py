# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy
from tvb.simulator.models.base import Model
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class Hopfield(ComponentWithWidget):
    taux: InArg[Union[float, numpy.ndarray]]
    tauT: InArg[Union[float, numpy.ndarray]]
    dynamic: InArg[Union[int, numpy.ndarray]]
    variables_of_interest: InArg[list]

    hopfield: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.hopfield import Hopfield
        return Hopfield

    def execute(self, ctx) -> None:
        hopfield = self.tvb_ht_class()

        set_values(self, hopfield)
        self.hopfield.value = hopfield
        print_component_summary(self.hopfield.value)

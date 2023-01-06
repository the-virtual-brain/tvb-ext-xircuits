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
class Epileptor(ComponentWithWidget):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    s: InArg[Union[float, numpy.ndarray]]
    x0: InArg[Union[float, numpy.ndarray]]
    Iext: InArg[Union[float, numpy.ndarray]]
    slope: InArg[Union[float, numpy.ndarray]]
    Iext2: InArg[Union[float, numpy.ndarray]]
    tau: InArg[Union[float, numpy.ndarray]]
    aa: InArg[Union[float, numpy.ndarray]]
    bb: InArg[Union[float, numpy.ndarray]]
    Kvf: InArg[Union[float, numpy.ndarray]]
    Kf: InArg[Union[float, numpy.ndarray]]
    Ks: InArg[Union[float, numpy.ndarray]]
    tt: InArg[Union[float, numpy.ndarray]]
    modification: InArg[Union[bool, numpy.ndarray]]
    variables_of_interest: InArg[list]

    epileptor: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.epileptor import Epileptor
        return Epileptor

    def execute(self, ctx) -> None:
        epileptor = self.tvb_ht_class()

        set_values(self, epileptor)
        self.epileptor.value = epileptor
        print_component_summary(self.epileptor.value)


@xai_component(color='rgb(101, 179, 46)')
class Epileptor2D(ComponentWithWidget):
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    c: InArg[Union[float, numpy.ndarray]]
    d: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    x0: InArg[Union[float, numpy.ndarray]]
    Iext: InArg[Union[float, numpy.ndarray]]
    slope: InArg[Union[float, numpy.ndarray]]
    Kvf: InArg[Union[float, numpy.ndarray]]
    Ks: InArg[Union[float, numpy.ndarray]]
    tt: InArg[Union[float, numpy.ndarray]]
    modification: InArg[Union[bool, numpy.ndarray]]
    variables_of_interest: InArg[list]

    epileptor2D: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.epileptor import Epileptor2D
        return Epileptor2D

    def execute(self, ctx) -> None:
        epileptor2D = self.tvb_ht_class()

        set_values(self, epileptor2D)
        self.epileptor2D.value = epileptor2D
        print_component_summary(self.epileptor2D.value)

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


# TODO: uncomment once EpileptorT is fixed in tvb-library
# @xai_component(color='rgb(101, 179, 46)')
# class EpileptorT(ComponentWithWidget):
#     a: InArg[float]
#     b: InArg[float]
#     c: InArg[float]
#     d: InArg[float]
#     r: InArg[float]
#     s: InArg[float]
#     x0: InArg[float]
#     Iext: InArg[float]
#     slope: InArg[float]
#     Iext2: InArg[float]
#     tau: InArg[float]
#     aa: InArg[float]
#     bb: InArg[float]
#     Kvf: InArg[float]
#     Kf: InArg[float]
#     Ks: InArg[float]
#     tt: InArg[float]
#     modification: InArg[int]
#     variables_of_interest: InArg[list]
#
#     epileptorT: OutArg[Model]
#
#     @property
#     def tvb_ht_class(self):
#         from tvb.simulator.models.epileptorT import EpileptorT
#         return EpileptorT
#
#     def execute(self, ctx) -> None:
#         epileptorT = self.tvb_ht_class()
#
#         set_values(self, epileptorT)
#         self.epileptorT.value = epileptorT
#         print_component_summary(self.epileptorT.value)

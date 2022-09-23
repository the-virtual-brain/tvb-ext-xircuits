# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


# TODO: uncomment once EpileptorT is fixed in tvb-library
# @xai_component(color='rgb(101, 179, 46)')
# class EpileptorT(Component):
#     from tvb.simulator.models.epileptorT import EpileptorT
#     a: InArg[list]
#     b: InArg[list]
#     c: InArg[list]
#     d: InArg[list]
#     r: InArg[list]
#     s: InArg[list]
#     x0: InArg[list]
#     Iext: InArg[list]
#     slope: InArg[list]
#     Iext2: InArg[list]
#     tau: InArg[list]
#     aa: InArg[list]
#     bb: InArg[list]
#     Kvf: InArg[list]
#     Kf: InArg[list]
#     Ks: InArg[list]
#     tt: InArg[list]
#     modification: InArg[list]
#     variables_of_interest: InArg[list]
#
#     epileptorT: OutArg[Model]
#
#     def __init__(self):
#         set_defaults(self, self.EpileptorT)
#
#     def execute(self, ctx) -> None:
#         epileptorT = self.EpileptorT()
#
#         set_values(self, epileptorT)
#         self.epileptorT.value = epileptorT
#         print_component_summary(self.epileptorT.value)

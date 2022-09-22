# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


# TODO: uncomment once KuramotoT is fixed in tvb-library
# @xai_component(color='rgb(101, 179, 46)')
# class KuramotoT(Component):
#     from tvb.simulator.models.kuramotoT import KuramotoT
#     omega: InArg[list]
#     variables_of_interest: InArg[list]
#
#     kuramotoT: OutArg[Model]
#
#     def __init__(self):
#         set_defaults(self, self.KuramotoT)
#
#     def execute(self, ctx) -> None:
#         kuramotoT = self.KuramotoT()
#
#         set_values(self, kuramotoT)
#         self.kuramotoT.value = kuramotoT
#         print_component_summary(self.kuramotoT.value)


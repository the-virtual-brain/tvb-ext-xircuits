# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
from tvb.simulator.backend.templates import MakoUtilMix
from xai_components.base import xai_component, OutArg
from xai_components.base_tvb import TVBComponent


@xai_component(color='rgb(219, 63, 28)')
class NbMPRBackend(TVBComponent):
    nbMPRBackend: OutArg[MakoUtilMix]

    def __init__(self):
        self.done = False

        self.nbMPRBackend = OutArg(None)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.backend.nb_mpr import NbMPRBackend
        return NbMPRBackend

    def execute(self, ctx) -> None:

        self.nbMPRBackend.value = self.tvb_ht_class()

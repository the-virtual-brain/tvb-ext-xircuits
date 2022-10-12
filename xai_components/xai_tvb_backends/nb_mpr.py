# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
from tvb.simulator.backend.templates import MakoUtilMix
from xai_components.base import xai_component, OutArg, Component


@xai_component(color='rgb(219, 63, 28)')
class NbMPRBackend(Component):
    nbMPRBackend: OutArg[MakoUtilMix]

    def __init__(self):
        self.done = False

        self.nbMPRBackend = OutArg(None)

    def execute(self, ctx) -> None:
        from tvb.simulator.backend.nb_mpr import NbMPRBackend

        self.nbMPRBackend.value = NbMPRBackend()

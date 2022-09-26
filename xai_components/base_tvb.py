# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#


from xai_components.base import Component
from xai_components.utils import set_defaults


class TVBComponent(Component):

    @property
    def tvb_ht_class(self):
        raise NotImplementedError

    def __init__(self):
        model = self.tvb_ht_class
        set_defaults(self, model)
        del model


class ComponentWithWidget(TVBComponent):
    """
    Used to flag a component that has an associate widget to be displayed in Xircuits UI for interactive setup.
    """

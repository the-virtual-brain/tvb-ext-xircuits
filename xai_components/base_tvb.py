# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#


from xai_components.base import Component


class ComponentWithWidget(Component):
    """
    Used to flag a component that has an associate widget to be displayed in Xircuits UI for interactive setup.
    """

    @property
    def tvb_ht_class(self):
        raise NotImplementedError

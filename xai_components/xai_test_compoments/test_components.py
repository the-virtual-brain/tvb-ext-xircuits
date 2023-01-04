# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy
from xai_components.base import InArg, Component, xai_component


@xai_component(color='rgb(85, 37, 130)')
class ANumpyTest(Component):
    numpy_code_str: InArg[numpy.ndarray]

    def __init__(self):
        self.done = False
        self.numpy_code_str = InArg(None)

    def execute(self, ctx) -> None:
        numpy_code = self.numpy_code_str.value
        print(f'Numpy code to be executed: {numpy_code}')
        numpy_arr = eval(numpy_code)
        print(f'Resulted numpy array: \n {numpy_arr}')

# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy  # DO NOT remove this; needed when Numpy Array Literals are used
import numpy as np
from inspect import isclass
from tvb.basic.neotraits._attr import NArray, Final
from tvb.basic.neotraits._core import HasTraits
from tvb.datatypes.equations import Equation

from xai_components.base import OutArg, InArg
from xai_components.logger.builder import get_logger

LOGGER = get_logger(__name__)

TYPE_STR = 'Type'
GID_STR = 'gid'


def should_set_attr(attr_value):
    """
    Check to see if an attribute should be set by the user or
    the default value should be kept
    """
    attr_name = attr_value.field_name
    if attr_name.lower() == 'gid':  # don't need to set the gid of an object in a Xircuits component
        return False
    if isinstance(attr_value, Final):  # if attr is Final, do not attempt to set it again
        return False

    return True


def set_defaults(component, tvb_datatype):
    # always set done attribute on False
    setattr(component, 'done', False)

    for attr in tvb_datatype.declarative_attrs:
        attr_value = getattr(tvb_datatype, attr)
        attr_default = attr_value.default
        print(type(attr_default))
        if issubclass(tvb_datatype, Equation) and callable(attr_default) and attr_default.__name__ == '<lambda>':
            attr_default = attr_default()
        elif isclass(attr_default) and issubclass(attr_value.field_type, HasTraits):
            attr_default = attr_default()
        if should_set_attr(attr_value):
            setattr(component, attr, InArg(attr_default))

    # also set the output arg
    out_arg_name = tvb_datatype.__name__
    out_arg_name = out_arg_name[0].lower() + out_arg_name[1:]
    setattr(component, out_arg_name, OutArg(None))


def set_values(component, tvb_object):
    cls = type(tvb_object)
    for attr in cls.declarative_attrs:
        attr_value = getattr(cls, attr)
        if should_set_attr(attr_value):
            xircuits_value = getattr(component, attr).value
            # if attribute in TVB is of type NArray, the value coming from Xircuits workflow must be converted to
            # numpy.array  to be able to set it on the TVB object
            if isinstance(attr_value, NArray):
                # if default for attr is None and was not set by user do not attempt to set it
                if xircuits_value is None:
                    continue
                if type(xircuits_value) is str:
                    xircuits_value = eval(xircuits_value)
                # if value set by a user not a numpy array, we must create it using the float/int provided
                if type(xircuits_value) != np.ndarray:
                    dtype = attr_value.dtype.name  # needed for NArrays of int type
                    xircuits_value = np.array(object=[xircuits_value], dtype=np.dtype(dtype))
                    # after converting to np.ndarryay, the resulting shape might be (1,1),
                    # which cannot be used in TVB computations, so a reshaping is needed
                if xircuits_value.shape == (1, 1):
                    xircuits_value = xircuits_value.reshape((1,))
            setattr(tvb_object, attr, xircuits_value)


def print_component_summary(traited_obj):
    component_summary = '\n== COMPONENT SUMMARY ==\n {\n'
    hastraits_summary = traited_obj.summary_info()

    # this if is needed because Connectivity doesn't add its type in its summary_info() method
    if TYPE_STR not in hastraits_summary.keys():
        cls = type(traited_obj)
        component_summary += f'"{TYPE_STR}": "{cls.__name__}",\n'

    for attr_name, attr in hastraits_summary.items():
        component_summary += f'"{attr_name}": "{attr}",\n'

    # this if is needed because Connectivity doesn't add its gid in its summary_info() method
    if GID_STR not in hastraits_summary.keys():
        gid_value = repr(traited_obj.gid)
        component_summary += f'"{GID_STR}": "{gid_value}"\n'
    component_summary += "}"
    LOGGER.info(component_summary)

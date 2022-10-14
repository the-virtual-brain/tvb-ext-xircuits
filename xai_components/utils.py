# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
import numpy as np
from tvb.basic.neotraits._attr import NArray, Final

from xai_components.base import OutArg, InArg

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
            # if attribute in TVB is of type NArray, the list coming from Xircuits workflow must be converted to
            # numpy.array  to be able to set the value on the TVB object
            if isinstance(attr_value, NArray):
                # if default for attr is None and was not set by user do not attempt to set it
                if not xircuits_value:  # use any to also test arrays with multiple elements, otherwise error
                    continue

                dtype = attr_value.dtype.name  # needed for NArrays of int type
                xircuits_value = [xircuits_value]  # need to convert it to list first
                xircuits_value = np.array(object=xircuits_value, dtype=np.dtype(dtype))

                # after converting to np.ndarryay, the resulting shape might be (1,1),
                # which cannot be used in TVB computations, so a reshaping is needed
                if xircuits_value.shape == (1, 1):
                    xircuits_value = xircuits_value.reshape((1,))
                # xircuits_value = xircuits_value.squeeze()  # squeeze result so it can be used in TVB computations
            setattr(tvb_object, attr, xircuits_value)


def print_component_summary(traited_obj):
    print('== COMPONENT SUMMARY ==')
    summary = traited_obj.summary_info()
    print("{")

    # this if is needed because Connectivity doesn't add its type in its summary_info() method
    if TYPE_STR not in summary.keys():
        cls = type(traited_obj)
        print(f'"{TYPE_STR}": "{cls.__name__}",')

    for attr_name, attr in summary.items():
        print(f'"{attr_name}": "{attr}",')

    # this if is needed because Connectivity doesn't add its gid in its summary_info() method
    if GID_STR not in summary.keys():
        gid_value = repr(traited_obj.gid)
        print(f'"{GID_STR}": "{gid_value}"')
    print("}")

# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

TYPE_STR = 'Type'
GID_STR = 'gid'


def print_component_summary(traited_obj):
    print('== COMPONENT SUMMARY ==')
    summary = traited_obj.summary_info()

    # this if is needed because Connectivity doesn't add its type in its summary_info() method
    if TYPE_STR not in summary.keys():
        cls = type(traited_obj)
        print(f'{TYPE_STR}: {cls.__name__}')

    for attr_name, attr in summary.items():
        print(f'{attr_name}: {attr}')

    # this if is needed because Connectivity doesn't add its gid in its summary_info() method
    if GID_STR not in summary.keys():
        gid_value = repr(traited_obj.gid)
        print(f'{GID_STR}: {gid_value}')

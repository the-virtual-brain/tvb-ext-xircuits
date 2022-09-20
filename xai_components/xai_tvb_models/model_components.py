# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy as np
from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary


@xai_component(color='rgb(101, 179, 46)')
class Epileptor(Component):
    a: InArg[list]
    b: InArg[list]
    c: InArg[list]
    d: InArg[list]
    r: InArg[list]
    s: InArg[list]
    x0: InArg[list]
    i_ext: InArg[list]
    slope: InArg[list]
    i_ext2: InArg[list]
    tau: InArg[list]
    aa: InArg[list]
    bb: InArg[list]
    kvf: InArg[list]
    kf: InArg[list]
    ks: InArg[list]
    ks: InArg[list]
    tt: InArg[list]
    modification: InArg[list]
    variables_of_interest: InArg[list]

    model: OutArg[Model]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.b = InArg(None)
        self.c = InArg(None)
        self.d = InArg(None)
        self.r = InArg(None)
        self.s = InArg(None)
        self.x0 = InArg(None)
        self.i_ext = InArg(None)
        self.slope = InArg(None)
        self.i_ext2 = InArg(None)
        self.tau = InArg(None)
        self.aa = InArg(None)
        self.bb = InArg(None)
        self.kvf = InArg(None)
        self.kf = InArg(None)
        self.ks = InArg(None)
        self.tt = InArg(None)
        self.modification = InArg(None)
        self.variables_of_interest = InArg(None)
        self.model = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.models.epileptor import Epileptor

        a = self.a.value
        b = self.b.value
        c = self.c.value
        d = self.d.value
        r = self.r.value
        s = self.s.value
        x0 = self.x0.value
        i_ext = self.i_ext.value
        slope = self.slope.value
        i_ext2 = self.i_ext2.value
        tau = self.tau.value
        aa = self.aa.value
        bb = self.bb.value
        kvf = self.kvf.value
        kf = self.kf.value
        ks = self.ks.value
        tt = self.tt.value
        modification = self.modification.value
        variables_of_interest = self.variables_of_interest.value

        # convert to numpy arrays
        a_arr = np.array(a)
        b_arr = np.array(b)
        c_arr = np.array(c)
        d_arr = np.array(d)
        r_arr = np.array(r)
        s_arr = np.array(s)
        x0_arr = np.array(x0)
        i_ext_arr = np.array(i_ext)
        slope_arr = np.array(slope)
        slope_arr = np.array(slope)
        i_ext2_arr = np.array(i_ext2)
        tau_arr = np.array(tau)
        aa_array = np.array(aa)
        bb_arr = np.array(bb)
        kvf_arr = np.array(kvf)
        kf_arr = np.array(kf)
        ks_arr = np.array(ks)
        tt_arr = np.array(tt)
        modification_arr = np.array(modification)

        epileptor = Epileptor(a=a_arr, b=b_arr, c=c_arr, d=d_arr, s=s_arr, x0=x0_arr, Iext=i_ext_arr, slope=slope_arr,
                              Iext2=i_ext2_arr, tau=tau_arr, aa=aa_array, bb=bb_arr, Kvf=kvf_arr, Kf=kf_arr, Ks=ks_arr,
                              tt=tt_arr, modification=modification_arr, variables_of_interest=variables_of_interest)

        self.model.value = epileptor
        print_component_summary(self.model.value)



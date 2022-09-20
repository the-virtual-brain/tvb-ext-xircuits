# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

import numpy as np
from tvb.simulator.coupling import Coupling
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary


@xai_component(color='rgb(0, 102, 178)')
class Linear(Component):
    a: InArg[list]
    b: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.b = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import Linear

        a = self.a.value
        b = self.b.value

        a_arr = np.array(a)
        b_arr = np.array(b)

        linear = Linear(a=a_arr, b=b_arr)
        self.coupling.value = linear
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class Scaling(Component):
    a: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import Scaling

        a = self.a.value
        a_arr = np.array(a)

        scaling = Scaling(a=a_arr)
        self.coupling.value = scaling
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class HyperbolicTangent(Component):
    a: InArg[list]
    b: InArg[list]
    midpoint: InArg[list]
    sigma: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.b = InArg(None)
        self.midpoint = InArg(None)
        self.sigma = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import HyperbolicTangent

        a = self.a.value
        b = self.b.value
        midpoint = self.midpoint.value
        sigma = self.sigma.value

        a_arr = np.array(a)
        b_arr = np.array(b)
        midpoint_arr = np.array(midpoint)
        sigma_arr = np.array(sigma)

        hyperbolic_tangent = HyperbolicTangent(a=a_arr, b=b_arr, midpoint=midpoint_arr, sigma=sigma_arr)
        self.coupling.value = hyperbolic_tangent
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class Sigmoidal(Component):
    cmin: InArg[list]
    cmax: InArg[list]
    midpoint: InArg[list]
    a: InArg[list]
    sigma: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.cmin = InArg(None)
        self.cmax = InArg(None)
        self.midpoint = InArg(None)
        self.a = InArg(None)
        self.sigma = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import Sigmoidal

        cmin = self.cmin.value
        cmax = self.cmax.value
        midpoint = self.midpoint.value
        a = self.a.value
        sigma = self.sigma.value

        cmin_arr = np.array(cmin)
        cmax_arr = np.array(cmax)
        midpoint_arr = np.array(midpoint)
        a_arr = np.array(a)
        sigma_arr = np.array(sigma)

        sigmoidal = Sigmoidal(cmin=cmin_arr, cmax=cmax_arr, midpoint=midpoint_arr, a=a_arr, sigma=sigma_arr)
        self.coupling.value = sigmoidal
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class SigmoidalJansenRit(Component):
    cmin: InArg[list]
    cmax: InArg[list]
    midpoint: InArg[list]
    r: InArg[list]
    a: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.cmin = InArg(None)
        self.cmax = InArg(None)
        self.midpoint = InArg(None)
        self.r = InArg(None)
        self.a = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import SigmoidalJansenRit

        cmin = self.cmin.value
        cmax = self.cmax.value
        midpoint = self.midpoint.value
        r = self.r.value
        a = self.a.value

        cmin_arr = np.array(cmin)
        cmax_arr = np.array(cmax)
        midpoint_arr = np.array(midpoint)
        r_arr = np.array(r)
        a_arr = np.array(a)

        sigmoidal_jansen_rit = SigmoidalJansenRit(cmin=cmin_arr, cmax=cmax_arr, midpoint=midpoint_arr, r=r_arr, a=a_arr)
        self.coupling.value = sigmoidal_jansen_rit
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class PreSigmoidal(Component):
    h: InArg[list]
    q: InArg[list]
    g: InArg[list]
    p: InArg[list]
    theta: InArg[list]
    dynamic: InArg[bool]
    global_t: InArg[bool]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.h = InArg(None)
        self.q = InArg(None)
        self.g = InArg(None)
        self.p = InArg(None)
        self.theta = InArg(None)
        self.dynamic = InArg(None)
        self.global_t = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import PreSigmoidal

        h = self.h.value
        q = self.q.value
        g = self.g.value
        p = self.p.value
        theta = self.theta.value
        dynamic = self.dynamic.value
        global_t = self.global_t.value

        h_arr = np.array(h)
        q_arr = np.array(q)
        g_arr = np.array(g)
        p_arr = np.array(p)
        theta_arr = np.array(theta)

        pre_sigmoidal = PreSigmoidal(H=h_arr, Q=q_arr, G=g_arr, P=p_arr, theta=theta_arr,dynamic=dynamic,
                                     globalT=global_t)
        self.coupling.value = pre_sigmoidal
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class Difference(Component):
    a: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import Difference

        a = self.a.value
        a_arr = np.array(a)

        difference = Difference(a=a_arr)
        self.coupling.value = difference
        print_component_summary(self.coupling.value)


@xai_component(color='rgb(0, 102, 178)')
class Kuramoto(Component):
    a: InArg[list]

    coupling: OutArg[Coupling]

    def __init__(self):
        self.done = False
        self.a = InArg(None)
        self.coupling = OutArg(None)

    def execute(self, ctx) -> None:
        # imports
        from tvb.simulator.coupling import Kuramoto

        a = self.a.value
        a_arr = np.array(a)

        kuramoto = Kuramoto(a=a_arr)
        self.coupling.value = kuramoto
        print_component_summary(self.coupling.value)

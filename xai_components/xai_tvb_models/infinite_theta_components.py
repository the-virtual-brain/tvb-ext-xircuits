# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, Component, InArg, OutArg
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(101, 179, 46)')
class MontbrioPazoRoxin(Component):
    from tvb.simulator.models.infinite_theta import MontbrioPazoRoxin
    tau: InArg[list]
    I: InArg[list]
    Delta: InArg[list]
    J: InArg[list]
    eta: InArg[list]
    Gamma: InArg[list]
    cr: InArg[list]
    cv: InArg[list]
    variables_of_interest: InArg[list]
    parameter_names: InArg[list]

    montbrioPazoRoxin: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.MontbrioPazoRoxin)

    def execute(self, ctx) -> None:
        montbrioPazoRoxin = self.MontbrioPazoRoxin()

        set_values(self, montbrioPazoRoxin)
        self.montbrioPazoRoxin.value = montbrioPazoRoxin
        print_component_summary(self.montbrioPazoRoxin.value)


@xai_component(color='rgb(101, 179, 46)')
class CoombesByrne(Component):
    from tvb.simulator.models.infinite_theta import CoombesByrne
    Delta: InArg[list]
    alpha: InArg[list]
    v_syn: InArg[list]
    k: InArg[list]
    eta: InArg[list]
    variables_of_interest: InArg[list]

    coombesByrne: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.CoombesByrne)

    def execute(self, ctx) -> None:
        coombesByrne = self.CoombesByrne()

        set_values(self, coombesByrne)
        self.coombesByrne.value = coombesByrne
        print_component_summary(self.coombesByrne.value)


@xai_component(color='rgb(101, 179, 46)')
class CoombesByrne2D(Component):
    from tvb.simulator.models.infinite_theta import CoombesByrne2D
    Delta: InArg[list]
    v_syn: InArg[list]
    k: InArg[list]
    eta: InArg[list]
    variables_of_interest: InArg[list]

    coombesByrne2D: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.CoombesByrne2D)

    def execute(self, ctx) -> None:
        coombesByrne2D = self.CoombesByrne2D()

        set_values(self, coombesByrne2D)
        self.coombesByrne2D.value = coombesByrne2D
        print_component_summary(self.coombesByrne2D.value)


@xai_component(color='rgb(101, 179, 46)')
class GastSchmidtKnosche_SD(Component):
    from tvb.simulator.models.infinite_theta import GastSchmidtKnosche_SD
    tau: InArg[list]
    tau_A: InArg[list]
    alpha: InArg[list]
    I: InArg[list]
    Delta: InArg[list]
    J: InArg[list]
    eta: InArg[list]
    cr: InArg[list]
    cv: InArg[list]
    variables_of_interest: InArg[list]

    gastSchmidtKnosche_SD: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.GastSchmidtKnosche_SD)

    def execute(self, ctx) -> None:
        gastSchmidtKnosche_SD = self.GastSchmidtKnosche_SD()

        set_values(self, gastSchmidtKnosche_SD)
        self.gastSchmidtKnosche_SD.value = gastSchmidtKnosche_SD
        print_component_summary(self.gastSchmidtKnosche_SD.value)


@xai_component(color='rgb(101, 179, 46)')
class GastSchmidtKnosche_SF(Component):
    from tvb.simulator.models.infinite_theta import GastSchmidtKnosche_SF
    tau: InArg[list]
    tau_A: InArg[list]
    alpha: InArg[list]
    I: InArg[list]
    Delta: InArg[list]
    J: InArg[list]
    eta: InArg[list]
    cr: InArg[list]
    cv: InArg[list]
    variables_of_interest: InArg[list]

    gastSchmidtKnosche_SF: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.GastSchmidtKnosche_SF)

    def execute(self, ctx) -> None:
        gastSchmidtKnosche_SF = self.GastSchmidtKnosche_SF()

        set_values(self, gastSchmidtKnosche_SF)
        self.gastSchmidtKnosche_SF.value = gastSchmidtKnosche_SF
        print_component_summary(self.gastSchmidtKnosche_SF.value)


@xai_component(color='rgb(101, 179, 46)')
class DumontGutkin(Component):
    from tvb.simulator.models.infinite_theta import DumontGutkin
    I_e: InArg[list]
    Delta_e: InArg[list]
    eta_e: InArg[list]
    tau_e: InArg[list]
    I_i: InArg[list]
    Delta_i: InArg[list]
    eta_i: InArg[list]
    tau_i: InArg[list]
    tau_s: InArg[list]
    J_ee: InArg[list]
    J_ei: InArg[list]
    J_ie: InArg[list]
    J_ii: InArg[list]
    Gamma: InArg[list]
    variables_of_interest: InArg[list]

    dumontGutkin: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.DumontGutkin)

    def execute(self, ctx) -> None:
        dumontGutkin = self.DumontGutkin()

        set_values(self, dumontGutkin)
        self.dumontGutkin.value = dumontGutkin
        print_component_summary(self.dumontGutkin.value)
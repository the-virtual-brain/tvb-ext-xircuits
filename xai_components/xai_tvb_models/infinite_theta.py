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
    tau: InArg[float]
    I: InArg[float]
    Delta: InArg[float]
    J: InArg[float]
    eta: InArg[float]
    Gamma: InArg[float]
    cr: InArg[float]
    cv: InArg[float]
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
    Delta: InArg[float]
    alpha: InArg[float]
    v_syn: InArg[float]
    k: InArg[float]
    eta: InArg[float]
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
    Delta: InArg[float]
    v_syn: InArg[float]
    k: InArg[float]
    eta: InArg[float]
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
    tau: InArg[float]
    tau_A: InArg[float]
    alpha: InArg[float]
    I: InArg[float]
    Delta: InArg[float]
    J: InArg[float]
    eta: InArg[float]
    cr: InArg[float]
    cv: InArg[float]
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
    tau: InArg[float]
    tau_A: InArg[float]
    alpha: InArg[float]
    I: InArg[float]
    Delta: InArg[float]
    J: InArg[float]
    eta: InArg[float]
    cr: InArg[float]
    cv: InArg[float]
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
    I_e: InArg[float]
    Delta_e: InArg[float]
    eta_e: InArg[float]
    tau_e: InArg[float]
    I_i: InArg[float]
    Delta_i: InArg[float]
    eta_i: InArg[float]
    tau_i: InArg[float]
    tau_s: InArg[float]
    J_ee: InArg[float]
    J_ei: InArg[float]
    J_ie: InArg[float]
    J_ii: InArg[float]
    Gamma: InArg[float]
    variables_of_interest: InArg[list]

    dumontGutkin: OutArg[Model]

    def __init__(self):
        set_defaults(self, self.DumontGutkin)

    def execute(self, ctx) -> None:
        dumontGutkin = self.DumontGutkin()

        set_values(self, dumontGutkin)
        self.dumontGutkin.value = dumontGutkin
        print_component_summary(self.dumontGutkin.value)
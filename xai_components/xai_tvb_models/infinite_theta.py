# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team

from tvb.simulator.models.base import Model
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class MontbrioPazoRoxin(ComponentWithWidget):
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

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import MontbrioPazoRoxin
        return MontbrioPazoRoxin

    def execute(self, ctx) -> None:
        montbrioPazoRoxin = self.tvb_ht_class()

        set_values(self, montbrioPazoRoxin)
        self.montbrioPazoRoxin.value = montbrioPazoRoxin
        print_component_summary(self.montbrioPazoRoxin.value)


@xai_component(color='rgb(101, 179, 46)')
class CoombesByrne(ComponentWithWidget):
    Delta: InArg[float]
    alpha: InArg[float]
    v_syn: InArg[float]
    k: InArg[float]
    eta: InArg[float]
    variables_of_interest: InArg[list]

    coombesByrne: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import CoombesByrne
        return CoombesByrne

    def execute(self, ctx) -> None:
        coombesByrne = self.tvb_ht_class()

        set_values(self, coombesByrne)
        self.coombesByrne.value = coombesByrne
        print_component_summary(self.coombesByrne.value)


@xai_component(color='rgb(101, 179, 46)')
class CoombesByrne2D(ComponentWithWidget):
    Delta: InArg[float]
    v_syn: InArg[float]
    k: InArg[float]
    eta: InArg[float]
    variables_of_interest: InArg[list]

    coombesByrne2D: OutArg[Model]

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import CoombesByrne2D
        return CoombesByrne2D

    def execute(self, ctx) -> None:
        coombesByrne2D = self.tvb_ht_class()

        set_values(self, coombesByrne2D)
        self.coombesByrne2D.value = coombesByrne2D
        print_component_summary(self.coombesByrne2D.value)


@xai_component(color='rgb(101, 179, 46)')
class GastSchmidtKnosche_SD(ComponentWithWidget):
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

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import GastSchmidtKnosche_SD
        return GastSchmidtKnosche_SD

    def execute(self, ctx) -> None:
        gastSchmidtKnosche_SD = self.tvb_ht_class()

        set_values(self, gastSchmidtKnosche_SD)
        self.gastSchmidtKnosche_SD.value = gastSchmidtKnosche_SD
        print_component_summary(self.gastSchmidtKnosche_SD.value)


@xai_component(color='rgb(101, 179, 46)')
class GastSchmidtKnosche_SF(ComponentWithWidget):
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

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import GastSchmidtKnosche_SF
        return GastSchmidtKnosche_SF

    def execute(self, ctx) -> None:
        gastSchmidtKnosche_SF = self.tvb_ht_class()

        set_values(self, gastSchmidtKnosche_SF)
        self.gastSchmidtKnosche_SF.value = gastSchmidtKnosche_SF
        print_component_summary(self.gastSchmidtKnosche_SF.value)


@xai_component(color='rgb(101, 179, 46)')
class DumontGutkin(ComponentWithWidget):
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

    @property
    def tvb_ht_class(self):
        from tvb.simulator.models.infinite_theta import DumontGutkin
        return DumontGutkin

    def execute(self, ctx) -> None:
        dumontGutkin = self.tvb_ht_class()

        set_values(self, dumontGutkin)
        self.dumontGutkin.value = dumontGutkin
        print_component_summary(self.dumontGutkin.value)

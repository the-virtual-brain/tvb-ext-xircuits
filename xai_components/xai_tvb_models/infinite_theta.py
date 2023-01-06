# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team

import numpy
from tvb.simulator.models.base import Model
from typing import Union
from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import ComponentWithWidget
from xai_components.utils import print_component_summary, set_values


@xai_component(color='rgb(101, 179, 46)')
class MontbrioPazoRoxin(ComponentWithWidget):
    tau: InArg[Union[float, numpy.ndarray]]
    I: InArg[Union[float, numpy.ndarray]]
    Delta: InArg[Union[float, numpy.ndarray]]
    J: InArg[Union[float, numpy.ndarray]]
    eta: InArg[Union[float, numpy.ndarray]]
    Gamma: InArg[Union[float, numpy.ndarray]]
    cr: InArg[Union[float, numpy.ndarray]]
    cv: InArg[Union[float, numpy.ndarray]]
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
    Delta: InArg[Union[float, numpy.ndarray]]
    alpha: InArg[Union[float, numpy.ndarray]]
    v_syn: InArg[Union[float, numpy.ndarray]]
    k: InArg[Union[float, numpy.ndarray]]
    eta: InArg[Union[float, numpy.ndarray]]
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
    Delta: InArg[Union[float, numpy.ndarray]]
    v_syn: InArg[Union[float, numpy.ndarray]]
    k: InArg[Union[float, numpy.ndarray]]
    eta: InArg[Union[float, numpy.ndarray]]
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
    tau: InArg[Union[float, numpy.ndarray]]
    tau_A: InArg[Union[float, numpy.ndarray]]
    alpha: InArg[Union[float, numpy.ndarray]]
    I: InArg[Union[float, numpy.ndarray]]
    Delta: InArg[Union[float, numpy.ndarray]]
    J: InArg[Union[float, numpy.ndarray]]
    eta: InArg[Union[float, numpy.ndarray]]
    cr: InArg[Union[float, numpy.ndarray]]
    cv: InArg[Union[float, numpy.ndarray]]
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
    tau: InArg[Union[float, numpy.ndarray]]
    tau_A: InArg[Union[float, numpy.ndarray]]
    alpha: InArg[Union[float, numpy.ndarray]]
    I: InArg[Union[float, numpy.ndarray]]
    Delta: InArg[Union[float, numpy.ndarray]]
    J: InArg[Union[float, numpy.ndarray]]
    eta: InArg[Union[float, numpy.ndarray]]
    cr: InArg[Union[float, numpy.ndarray]]
    cv: InArg[Union[float, numpy.ndarray]]
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
    I_e: InArg[Union[float, numpy.ndarray]]
    Delta_e: InArg[Union[float, numpy.ndarray]]
    eta_e: InArg[Union[float, numpy.ndarray]]
    tau_e: InArg[Union[float, numpy.ndarray]]
    I_i: InArg[Union[float, numpy.ndarray]]
    Delta_i: InArg[Union[float, numpy.ndarray]]
    eta_i: InArg[Union[float, numpy.ndarray]]
    tau_i: InArg[Union[float, numpy.ndarray]]
    tau_s: InArg[Union[float, numpy.ndarray]]
    J_ee: InArg[Union[float, numpy.ndarray]]
    J_ei: InArg[Union[float, numpy.ndarray]]
    J_ie: InArg[Union[float, numpy.ndarray]]
    J_ii: InArg[Union[float, numpy.ndarray]]
    Gamma: InArg[Union[float, numpy.ndarray]]
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

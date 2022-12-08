# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#
from tvb.basic.neotraits.api import EnumAttr
from tvb.datatypes.equations import HRFKernelEquation
from tvb.datatypes.projections import ProjectionSurfaceEEG, ProjectionSurfaceMEG, ProjectionSurfaceSEEG
from tvb.datatypes.region_mapping import RegionMapping
from tvb.datatypes.sensors import SensorsEEG, SensorsInternal, SensorsMEG
from tvb.simulator.noise import Noise

from xai_components.base import xai_component, InArg, OutArg, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import print_component_summary, set_defaults, set_values


@xai_component(color='rgb(247, 158, 27)')
class Raw(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    raw: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import Raw
        return Raw

    def execute(self, ctx) -> None:
        raw = self.tvb_ht_class()
        set_values(self, raw)

        monitors_list = self.previous_monitors.value
        monitors_list.append(raw)
        self.raw.value = monitors_list
        print_component_summary(self.raw.value[-1]) # -1 to print the latest added monitor, i.e. the current monitor


@xai_component(color='rgb(247, 158, 27)')
class RawVoi(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    rawVoi: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import RawVoi
        return RawVoi

    def execute(self, ctx) -> None:
        rawVoi = self.tvb_ht_class()
        set_values(self, rawVoi)

        monitors_list = self.previous_monitors.value
        monitors_list.append(rawVoi)
        self.rawVoi.value = monitors_list
        print_component_summary(self.rawVoi.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class SubSample(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    subSample: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import SubSample
        return SubSample

    def execute(self, ctx) -> None:
        subSample = self.tvb_ht_class()
        set_values(self, subSample)

        monitors_list = self.previous_monitors.value
        monitors_list.append(subSample)
        self.subSample.value = monitors_list
        print_component_summary(self.subSample.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class SpatialAverage(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    spatial_mask: InArg[list]
    default_mask: InArg[EnumAttr]

    spatialAverage: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import SpatialAverage
        return SpatialAverage

    def execute(self, ctx) -> None:
        spatialAverage = self.tvb_ht_class()
        set_values(self, spatialAverage)

        monitors_list = self.previous_monitors.value
        monitors_list.append(spatialAverage)
        self.spatialAverage.value = monitors_list
        print_component_summary(self.spatialAverage.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class GlobalAverage(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    globalAverage: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import GlobalAverage
        return GlobalAverage

    def execute(self, ctx) -> None:
        globalAverage = self.tvb_ht_class()
        set_values(self, globalAverage)

        monitors_list = self.previous_monitors.value
        monitors_list.append(globalAverage)
        self.globalAverage.value = monitors_list
        print_component_summary(self.globalAverage.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class TemporalAverage(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    temporalAverage: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import TemporalAverage
        return TemporalAverage

    def execute(self, ctx) -> None:
        temporalAverage = self.tvb_ht_class()
        set_values(self, temporalAverage)

        monitors_list = self.previous_monitors.value
        monitors_list.append(temporalAverage)
        self.temporalAverage.value = monitors_list
        print_component_summary(self.temporalAverage.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class AfferentCoupling(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    afferentCoupling: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import AfferentCoupling
        return AfferentCoupling

    def execute(self, ctx) -> None:
        afferentCoupling = self.tvb_ht_class()
        set_values(self, afferentCoupling)

        monitors_list = self.previous_monitors.value
        monitors_list.append(afferentCoupling)
        self.afferentCoupling.value = monitors_list
        print_component_summary(self.afferentCoupling.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class AfferentCouplingTemporalAverage(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    afferentCouplingTemporalAverage: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import AfferentCouplingTemporalAverage
        return AfferentCouplingTemporalAverage

    def execute(self, ctx) -> None:
        afferentCouplingTemporalAverage = self.tvb_ht_class()
        set_values(self, afferentCouplingTemporalAverage)

        monitors_list = self.previous_monitors.value
        monitors_list.append(afferentCouplingTemporalAverage)
        self.afferentCouplingTemporalAverage.value = monitors_list
        print_component_summary(self.afferentCouplingTemporalAverage.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class EEG(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    region_mapping: InArg[RegionMapping]
    obsnoise: InArg[Noise]
    projection: InCompArg[ProjectionSurfaceEEG]
    reference: InArg[str]
    sensors: InCompArg[SensorsEEG]
    sigma: InArg[float]

    eEG: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import EEG
        return EEG

    def execute(self, ctx) -> None:
        eEG = self.tvb_ht_class()
        set_values(self, eEG)

        monitors_list = self.previous_monitors.value
        monitors_list.append(eEG)
        self.eEG.value = monitors_list
        print_component_summary(self.eEG.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class MEG(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    region_mapping: InArg[RegionMapping]
    obsnoise: InArg[Noise]
    projection: InCompArg[ProjectionSurfaceMEG]
    sensors: InCompArg[SensorsMEG]

    mEG: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import MEG
        return MEG

    def execute(self, ctx) -> None:
        mEG = self.tvb_ht_class()
        set_values(self, mEG)

        monitors_list = self.previous_monitors.value
        monitors_list.append(mEG)
        self.mEG.value = monitors_list
        print_component_summary(self.mEG.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class iEEG(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    region_mapping: InArg[RegionMapping]
    obsnoise: InArg[Noise]
    projection: InCompArg[ProjectionSurfaceSEEG]
    sigma: InArg[float]
    sensors: InCompArg[SensorsInternal]

    iEEG: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import iEEG
        return iEEG

    def execute(self, ctx) -> None:
        iEEG = self.tvb_ht_class()
        set_values(self, iEEG)

        monitors_list = self.previous_monitors.value
        monitors_list.append(iEEG)
        self.iEEG.value = monitors_list
        print_component_summary(self.iEEG.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class Bold(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    hrf_kernel: InArg[HRFKernelEquation]
    hrf_length: InArg[float]

    bold: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import Bold
        return Bold

    def execute(self, ctx) -> None:
        bold = self.tvb_ht_class()
        set_values(self, bold)

        monitors_list = self.previous_monitors.value
        monitors_list.append(bold)
        self.bold.value = monitors_list
        print_component_summary(self.bold.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class BoldRegionROI(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]
    hrf_kernel: InArg[HRFKernelEquation]
    hrf_length: InArg[float]

    boldRegionROI: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import BoldRegionROI
        return BoldRegionROI

    def execute(self, ctx) -> None:
        boldRegionROI = self.tvb_ht_class()
        set_values(self, boldRegionROI)

        monitors_list = self.previous_monitors.value
        monitors_list.append(boldRegionROI)
        self.boldRegionROI.value = monitors_list
        print_component_summary(self.boldRegionROI.value[-1])


@xai_component(color='rgb(247, 158, 27)')
class ProgressLogger(TVBComponent):
    previous_monitors: InArg[list]
    period: InArg[float]
    variables_of_interest: InArg[list]

    progressLogger: OutArg[list]

    def __init__(self):
        self.previous_monitors = InArg([])
        set_defaults(self, self.tvb_ht_class)

    @property
    def tvb_ht_class(self):
        from tvb.simulator.monitors import ProgressLogger
        return ProgressLogger

    def execute(self, ctx) -> None:
        progressLogger = self.tvb_ht_class()
        set_values(self, progressLogger)

        monitors_list = self.previous_monitors.value
        monitors_list.append(progressLogger)
        self.progressLogger.value = monitors_list
        print_component_summary(self.progressLogger.value[-1])
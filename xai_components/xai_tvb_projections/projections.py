# -*- coding: utf-8 -*-
#
# "TheVirtualBrain - Widgets" package
#
# (c) 2022-2023, TVB Widgets Team
#

from tvb.datatypes.projections import ProjectionSurfaceEEG, ProjectionSurfaceMEG, ProjectionSurfaceSEEG
from tvb.datatypes.sensors import SensorsEEG, SensorsMEG, SensorsInternal
from tvb.datatypes.surfaces import Surface
from xai_components.base import xai_component, InArg, OutArg, Component, InCompArg
from xai_components.utils import print_component_summary


@xai_component(color='rgb(67, 47, 106)')
class ProjectionSurfaceEEG(Component):
    file_path: InArg[str]
    sources: InCompArg[Surface]
    sensors: InCompArg[SensorsEEG]

    projectionSurfaceEEG: OutArg[ProjectionSurfaceEEG]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.projections import ProjectionSurfaceEEG
        return ProjectionSurfaceEEG

    def __init__(self):
        self.done = False

        self.file_path = InArg(None)
        self.sources = InCompArg(None)
        self.sensors = InCompArg(None)
        self.projectionSurfaceEEG = OutArg(None)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'projection_eeg_65_surface_16k.npy'  # default from tvb_data
        projectionSurfaceEEG = self.ProjectionSurfaceEEG.from_file(source_file=file_path)

        projectionSurfaceEEG.sources = self.sources.value
        projectionSurfaceEEG.sensors = self.sensors.value
        projectionSurfaceEEG.configure()

        self.projectionSurfaceEEG.value = projectionSurfaceEEG
        print_component_summary(self.projectionSurfaceEEG.value)


@xai_component(color='rgb(67, 47, 106)')
class ProjectionSurfaceMEG(Component):
    file_path: InArg[str]
    sources: InCompArg[Surface]
    sensors: InCompArg[SensorsMEG]

    projectionSurfaceMEG: OutArg[ProjectionSurfaceMEG]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.projections import ProjectionSurfaceMEG
        return ProjectionSurfaceMEG

    def __init__(self):
        self.done = False

        self.file_path = InArg(None)
        self.sources = InCompArg(None)
        self.sensors = InCompArg(None)
        self.projectionSurfaceMEG = OutArg(None)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'projection_meg_276_surface_16k.npy'  # default from tvb_data
        projectionSurfaceMEG = self.tvb_ht_class.from_file(source_file=file_path)

        projectionSurfaceMEG.sources = self.sources.value
        projectionSurfaceMEG.sensors = self.sensors.value
        projectionSurfaceMEG.configure()

        self.projectionSurfaceMEG.value = projectionSurfaceMEG
        print_component_summary(self.projectionSurfaceMEG.value)


@xai_component(color='rgb(67, 47, 106)')
class ProjectionSurfaceSEEG(Component):
    file_path: InArg[str]
    sources: InCompArg[Surface]
    sensors: InCompArg[SensorsInternal]

    projectionSurfaceSEEG: OutArg[ProjectionSurfaceSEEG]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.projections import ProjectionSurfaceSEEG
        return ProjectionSurfaceSEEG

    def __init__(self):
        self.done = False

        self.file_path = InArg(None)
        self.sources = InCompArg(None)
        self.sensors = InCompArg(None)
        self.projectionSurfaceSEEG = OutArg(None)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'projection_seeg_588_surface_16k.npy'  # default from tvb_data
        projectionSurfaceSEEG = self.tvb_ht_class.from_file(source_file=file_path)

        projectionSurfaceSEEG.sources = self.sources.value
        projectionSurfaceSEEG.sensors = self.sensors.value
        projectionSurfaceSEEG.configure()

        self.projectionSurfaceSEEG.value = projectionSurfaceSEEG
        print_component_summary(self.projectionSurfaceSEEG.value)

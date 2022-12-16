from tvb.datatypes.surfaces import Surface
from xai_components.base import xai_component, InArg, OutArg, InCompArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import set_values, print_component_summary, set_defaults


@xai_component(color='rgb(0, 116, 92)')
class WhiteMatterSurface(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    whiteMatterSurface: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import WhiteMatterSurface
        return WhiteMatterSurface

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'cortex_16384.zip'  # default from tvb_data
        whiteMatterSurface = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, whiteMatterSurface)
        whiteMatterSurface.configure()

        self.whiteMatterSurface.value = whiteMatterSurface
        print_component_summary(self.whiteMatterSurface.value)


@xai_component(color='rgb(0, 116, 92)')
class CorticalSurface(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    corticalSurface: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import CorticalSurface
        return CorticalSurface

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'cortex_16384.zip'  # default from tvb_data
        corticalSurface = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, corticalSurface)
        corticalSurface.configure()

        self.corticalSurface.value = corticalSurface
        print_component_summary(self.corticalSurface.value)


@xai_component(color='rgb(0, 116, 92)')
class SkinAir(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    skinAir: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import SkinAir
        return SkinAir

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'outer_skin_4096.zip'  # default from tvb_data
        skinAir = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, skinAir)
        skinAir.configure()

        self.skinAir.value = skinAir
        print_component_summary(self.skinAir.value)


@xai_component(color='rgb(0, 116, 92)')
class BrainSkull(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    brainSkull: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import BrainSkull
        return BrainSkull

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'inner_skull_4096.zip'  # default from tvb_data
        brainSkull = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, brainSkull)
        brainSkull.configure()

        self.brainSkull.value = brainSkull
        print_component_summary(self.brainSkull.value)


@xai_component(color='rgb(0, 116, 92)')
class SkullSkin(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    skullSkin: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import SkullSkin
        return SkullSkin

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'outer_skull_4096.zip'  # default from tvb_data
        skullSkin = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, skullSkin)
        skullSkin.configure()

        self.skullSkin.value = skullSkin
        print_component_summary(self.skullSkin.value)


@xai_component(color='rgb(0, 116, 92)')
class EEGCap(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    eEGCap: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import EEGCap
        return EEGCap

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'scalp_1082.zip'  # default from tvb_data
        eEGCap = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, eEGCap)
        eEGCap.configure()

        self.eEGCap.value = eEGCap
        print_component_summary(self.eEGCap.value)


@xai_component(color='rgb(0, 116, 92)')
class FaceSurface(TVBComponent):
    file_path: InArg[str]
    triangle_normals: InArg[list]
    hemisphere_mask: InArg[list]
    zero_based_triangles: InCompArg[bool]

    faceSurface: OutArg[Surface]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.surfaces import FaceSurface
        return FaceSurface

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'face_8614.zip'  # default from tvb_data
        faceSurface = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, faceSurface)
        faceSurface.configure()

        self.faceSurface.value = faceSurface
        print_component_summary(self.faceSurface.value)

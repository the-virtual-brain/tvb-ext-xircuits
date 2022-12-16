from tvb.datatypes.sensors import Sensors

from xai_components.base import xai_component, InArg, OutArg
from xai_components.base_tvb import TVBComponent
from xai_components.utils import set_values, print_component_summary, set_defaults


@xai_component(color='rgb(0, 116, 149)')
class SensorsEEG(TVBComponent):
    file_path: InArg[str]
    has_orientation: InArg[bool]
    orientations: InArg[list]
    usable: InArg[list]

    sensorsEEG: OutArg[Sensors]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.sensors import SensorsEEG
        return SensorsEEG

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'eeg_brainstorm_65.txt'  # default from tvb_data
        sensorsEEG = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, sensorsEEG)
        sensorsEEG.configure()

        self.sensorsEEG.value = sensorsEEG
        print_component_summary(self.sensorsEEG.value)


@xai_component(color='rgb(0, 116, 149)')
class SensorsMEG(TVBComponent):
    file_path: InArg[str]
    usable: InArg[list]

    sensorsMEG: OutArg[Sensors]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.sensors import SensorsMEG
        return SensorsMEG

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'meg_151.txt.bz2'  # default from tvb_data
        sensorsMEG = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, sensorsMEG)
        sensorsMEG.configure()

        self.sensorsMEG.value = sensorsMEG
        print_component_summary(self.sensorsMEG.value)


@xai_component(color='rgb(0, 116, 149)')
class SensorsInternal(TVBComponent):
    file_path: InArg[str]
    has_orientation: InArg[bool]
    orientations: InArg[list]
    usable: InArg[list]

    sensorsInternal: OutArg[Sensors]

    @property
    def tvb_ht_class(self):
        from tvb.datatypes.sensors import SensorsInternal
        return SensorsInternal

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.tvb_ht_class)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if not file_path:
            file_path = 'seeg_39.txt.bz2'  # default from tvb_data
        sensorsInternal = self.tvb_ht_class.from_file(source_file=file_path)
        set_values(self, sensorsInternal)
        sensorsInternal.configure()

        self.sensorsInternal.value = sensorsInternal
        print_component_summary(self.sensorsInternal.value)
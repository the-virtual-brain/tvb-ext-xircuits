from tvb.datatypes.sensors import Sensors

from xai_components.base import xai_component, InArg, OutArg, Component
from xai_components.utils import set_values, print_component_summary, set_defaults


@xai_component(color='rgb(0, 102, 178)')
class SensorsEEG(Component):
    from tvb.datatypes.sensors import SensorsEEG
    file_path: InArg[str]
    labels: InArg[list]
    locations: InArg[list]
    has_orientation: InArg[bool]
    orientations: InArg[list]
    number_of_sensors: InArg[int]
    usable: InArg[list]

    sensorsEEG: OutArg[Sensors]

    def __init__(self):
        self.file_path = InArg(None)
        set_defaults(self, self.SensorsEEG)

    def execute(self, ctx) -> None:
        file_path = self.file_path.value
        if file_path:
            sensorsEEG = self.SensorsEEG.from_file(source_file=file_path)
        else:
            sensorsEEG = self.SensorsEEG.from_file()
        set_values(self, sensorsEEG)
        sensorsEEG.configure()

        self.sensorsEEG.value = sensorsEEG
        print_component_summary(self.sensorsEEG.value)




from xai_components.base import xai_component, Component, InArg, OutArg
from typing import Union

@xai_component(color='rgb(101, 179, 46)')
class MPRSdeCupy(Component):
    G: InArg[Union[float, list]]
    dt: InArg[float]
    dt_bold: InArg[float]
    J: InArg[Union[float, list]]
    eta: InArg[Union[float, list]]
    tau: InArg[float]
    delta: InArg[float]
    tr: InArg[float]
    noise_amp: InArg[Union[float, list]]
    same_noise_per_sim: InArg[bool]
    sti_apply: InArg[bool]
    iapp: InArg[Union[float, list]]
    t_start: InArg[float]
    t_cut: InArg[float]
    t_end: InArg[float]
    num_nodes: InArg[int]
    weights: InArg[list]
    rv_decimate: InArg[int]
    output: InArg[str]
    RECORD_RV: InArg[bool]
    RECORD_BOLD: InArg[bool]
    RECORD_AVG_r: InArg[bool]
    num_sim: InArg[int]
    method: InArg[str]
    engine: InArg[str]
    seed: InArg[int]
    dtype: InArg[str]
    initial_state: InArg[list]
    same_initial_state: InArg[bool]

    model: OutArg[any]
    time_series_key: OutArg[dict]

    def __init__(self):
        super().__init__()

    def execute(self, ctx) -> None:
        from vbi.models.cupy.mpr import MPR_sde

        keys = ["G", "dt", "dt_bold", "J", "eta", "tau", "delta", "tr", "noise_amp", "same_noise_per_sim", "sti_apply",
                "iapp", "t_start", "t_cut", "t_end", "num_nodes", "weights", "rv_decimate", "output", "RECORD_RV",
                "RECORD_BOLD", "RECORD_AVG_r", "num_sim", "method", "engine", "seed", "dtype", "initial_state",
                "same_initial_state"]
        params = {}
        for key in keys:
            param = getattr(self, key, None)
            if param.value is not None:
                params[key] = param.value

        self.model.value = MPR_sde(par=params)
        self.time_series_key.value = {"t": "rv_t", "x": "rv_d"} if self.model.value.RECORD_RV \
            else {"t": "fmri_t", "x": "fmri_d"}
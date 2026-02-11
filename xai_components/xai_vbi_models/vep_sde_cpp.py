from xai_components.base import xai_component, Component, InArg, OutArg
from typing import Union

@xai_component(color='rgb(101, 179, 46)')
class VEPSdeCpp(Component):
    G: InArg[Union[float, list]]
    seed: InArg[int]
    initial_state: InArg[list]
    weights: InArg[list]
    tau: InArg[float]
    eta: InArg[Union[int, float, list]]
    noise_sigma: InArg[float]
    iext: InArg[Union[int, float, list]]
    dt: InArg[float]
    tend: InArg[float]
    tcut: InArg[float]
    noise_seed: InArg[int]
    record_step: InArg[int]
    method: InArg[str]
    output: InArg[str]

    model: OutArg[any]
    time_series_key: OutArg[dict]

    def execute(self, ctx) -> None:
        from vbi.models.cpp.vep import VEP_sde

        keys = ["G", "seed", "initial_state", "weights", "tau", "eta", "noise_sigma", "iext", "dt", "tend", "tcut",
                "noise_seed", "record_step", "method", "output"]
        params = {}
        for key in keys:
            param = getattr(self, key, None)
            if param.value is not None:
                params[key] = param.value
        self.model.value = VEP_sde(par=params)
        self.time_series_key.value = {"t": "t", "x": "x"}
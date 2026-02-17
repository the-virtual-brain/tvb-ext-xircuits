from xai_components.base import xai_component, Component, InArg, OutArg
from typing import Union

@xai_component(color='rgb(101, 179, 46)')
class JRSdeCpp(Component):
    G: InArg[Union[float, list]]
    A: InArg[Union[float, list]]
    B: InArg[Union[float, list]]
    a: InArg[Union[float, list]]
    b: InArg[Union[float, list]]
    noise_mu: InArg[Union[float, list]]
    noise_std: InArg[Union[float, list]]
    vmax: InArg[float]
    v0: InArg[Union[float, list]]
    r: InArg[Union[float, list]]
    initial_state: InArg[list]
    weights: InArg[list]
    C0: InArg[Union[float, list]]
    C1: InArg[Union[float, list]]
    C2: InArg[Union[float, list]]
    C3: InArg[Union[float, list]]
    noise_seed: InArg[int] #?type
    seed: InArg[int]
    dt: InArg[float]
    method: InArg[str]
    t_transition: InArg[float]
    t_end: InArg[float]
    output: InArg[str]
    RECORD_AVG: InArg[bool]

    model: OutArg[any]
    time_series_key: OutArg[dict]

    def execute(self, ctx):
        from vbi.models.cpp.jansen_rit import JR_sde

        keys = ["noise_seed", "seed", "G", "weights", "A", "B", "a", "b", "noise_mu", "noise_std", "vmax", "v0", "r",
                "C0", "C1", "C2", "C3", "dt", "method", "t_transition", "t_end", "output", "RECORD_AVG",
                "initial_state"]
        params = {}
        for key in keys:
            param = getattr(self, key, None)
            if param.value is not None:
                params[key] = param.value

        self.model.value = JR_sde(par=params)
        self.time_series_key.value = {"t": "t", "x": "x"}
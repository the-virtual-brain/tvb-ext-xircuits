from xai_components.base import xai_component, Component, InArg, OutArg
from vbi.models.cupy.jansen_rit import JR_sde
from typing import Union

@xai_component(color='rgb(101, 179, 46)')
class JRSdeCupy(Component):
    G: InArg[Union[float, list]]
    A: InArg[Union[float, list]]
    B: InArg[Union[float, list]]
    v: InArg[Union[float, list]]
    r: InArg[Union[float, list]]
    v0: InArg[Union[float, list]]
    vmax: InArg[float]
    C0: InArg[Union[float, list]]
    C1: InArg[Union[float, list]]
    C2: InArg[Union[float, list]]
    C3: InArg[Union[float, list]]
    a: InArg[Union[float, list]]
    b: InArg[Union[float, list]]
    mu: InArg[Union[float, list]]
    noise_amp: InArg[Union[float, list]]
    decimate: InArg[[int]]
    dt: InArg[float]
    t_end: InArg[float]
    t_cut: InArg[float]
    engine: InArg[str]
    method: InArg[str]
    num_sim: InArg[int]
    weights: InArg[list]
    dtype: InArg[str]
    seed: InArg[int]
    initial_state: InArg[list]
    same_initial_state: InArg[bool]
    same_noise_per_sim: InArg[bool]

    model: OutArg[JR_sde]

    def execute(self, ctx):
        keys = ["G", "A", "B", "v", "r", "v0", "vmax", "C0", "C1", "C2", "C3", "a", "b", "mu", "noise_amp",
                  "decimate", "dt", "t_end", "t_cut", "engine", "method", "num_sim", "weights", "dtype", "seed",
                  "initial_state", "same_initial_state", "same_noise_per_sim"]
        params = {}
        for key in keys:
            param = getattr(self, key, None)
            if param.value is not None:
                params[key] = param.value

        self.model.value = JR_sde(par=params)


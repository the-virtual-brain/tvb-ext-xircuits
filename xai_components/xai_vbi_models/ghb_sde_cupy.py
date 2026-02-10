from xai_components.base import xai_component, Component, InArg, OutArg
from typing import Union

@xai_component(color='rgb(101, 179, 46)')
class GHBSdeCupy(Component):
    G: InArg[Union[float, list]]
    t_cut: InArg[float]
    dt: InArg[float]
    eta: InArg[int]
    num_sim: InArg[int]
    sigma: InArg[float]
    seed: InArg[int]
    decimate: InArg[[int]]
    omega: InArg[Union[float, list]]
    t_end: InArg[float]
    engine: InArg[str]
    weights: InArg[list]
    dtype: InArg[str]
    method: InArg[str]
    output: InArg[str]
    initial_state: InArg[list]
    same_initial_state: InArg[bool]

    model: OutArg[any]
    time_series_key: OutArg[dict]

    def execute(self, ctx):
        from vbi.models.cupy.ghb import GHB_sde

        keys = ["G", "t_cut", "dt", "eta", "num_sim", "sigma", "seed", "decimate", "omega", "t_end", "engine",
                "weights", "dtype", "method", "output", "initial_state", "same_initial_state"]
        params = {}
        for key in keys:
            param = getattr(self, key, None)
            if param.value is not None:
                params[key] = param.value

        self.model.value = GHB_sde(par=params)
        self.time_series_key.value = {"t": "t", "x": "bold"}
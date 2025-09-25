from xai_components.base import xai_component, Component, InArg, OutArg
from vbi.models.cupy.jansen_rit import JR_sde
from typing import Union
import numpy

@xai_component(color='rgb(101, 179, 46)')
class JRSdeCupy(Component):
    G: InArg[Union[float, numpy.ndarray]]
    A: InArg[Union[float, numpy.ndarray]]
    B: InArg[Union[float, numpy.ndarray]]
    v: InArg[Union[float, numpy.ndarray]]
    r: InArg[Union[float, numpy.ndarray]]
    v0: InArg[Union[float, numpy.ndarray]]
    vmax: InArg[float]
    C0: InArg[Union[float, numpy.ndarray]]
    C1: InArg[Union[float, numpy.ndarray]]
    C2: InArg[Union[float, numpy.ndarray]]
    C3: InArg[Union[float, numpy.ndarray]]
    a: InArg[Union[float, numpy.ndarray]]
    b: InArg[Union[float, numpy.ndarray]]
    mu: InArg[Union[float, numpy.ndarray]]
    noise_amp: InArg[Union[float, numpy.ndarray]]
    decimate: InArg[[int]]
    dt: InArg[float]
    t_end: InArg[float]
    t_cut: InArg[float]
    engine: InArg[str]
    method: InArg[str]
    num_sim: InArg[int]
    weights: InArg[numpy.ndarray]
    dtype: InArg[str]
    seed: InArg[int]
    initial_state: InArg[numpy.ndarray]
    same_initial_state: InArg[bool]
    same_noise_per_sim: InArg[bool]

    model: OutArg[JR_sde]
    dt_param: OutArg[float] # time step - used to compute Sampling frequency for extract features

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
        self.dt_param.value = self.dt.value if self.dt.value else self.model.value.get_default_parameters()['dt']


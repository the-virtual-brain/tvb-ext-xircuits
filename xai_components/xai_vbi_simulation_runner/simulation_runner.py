from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from multiprocessing import Pool
from copy import deepcopy
from typing import Literal

@xai_component(color='rgb(220, 5, 45)')
class SimulationRunner(Component):
    backend: InArg[Literal['cupy', 'cpp']]
    model: InArg[any]               # union between vbi models
    theta: InArg[torch.Tensor]
    theta_names: InArg[list]
    cfg: InArg[dict]
    num_workers: InArg[int]
    time_series_key: InArg[str]

    stat_vec: OutArg[np.ndarray]    # (N, F)

    def __init__(self):
        super().__init__()
        self.backend.value = "cupy"
        self.num_workers.value = 1

    def execute(self, ctx):
        import vbi

        # theta -> numpy
        th = self.theta.value
        theta_np = th.detach().cpu().numpy() if hasattr(th, "detach") else np.asarray(th)
        theta_np = theta_np.astype(float, copy=False)
        num_sim, num_params = theta_np.shape

        if num_params != len(self.theta_names.value):
            raise ValueError(f"Theta has {num_params} columns, but theta_names has {len(self.theta_names.value)}.")
        idx = {par: index for index, par in enumerate(self.theta_names.value)}

        #TODO should we expose the sampling frequency as a parameter(InArg[int, float]) and let the user choose the
        #  value he wants?
        fs = 1000.0 / float(self.model.value.dt)

        # infer nn for broadcasting
        nn = int(np.asarray(self.model.value.weights).shape[0])

        #TODO How should we shape/broadcast special params (e.g., C0–C3)?
        #  Current workaround: np.tile to (number_nodes, number_sim) for node-wise params (see lines 57, 77)
        nodewise = {"C0", "C1", "C2", "C3"}  # temporary

        model = self.model.value
        x = self.time_series_key.value

        if self.backend.value == "cpp":
            #TODO Can we have a get_params() function on models?
            # We need to read the user set params from Model components (e.g. JRSdeCupy) without using private _par
            base = model._par  # temporary

            def one(sim_i: int):
                par_i = deepcopy(base)
                for col, par in idx.items():
                    val = theta_np[sim_i, par]
                    if col in nodewise:
                        par_i[par] = np.full(nn, val, dtype=float)
                    else:
                        par_i[par] = val
                model_class = model.__class__
                data = model_class(par_i).run()
                ts = data[x]
                stat_vec = vbi.extract_features(ts=[ts], cfg=self.cfg.value, fs=fs,
                                          n_workers=1, verbose=False).values
                return stat_vec[0]

            with Pool(processes=self.num_workers.value) as pool:
                rows = pool.map(one, range(num_sim))

            x = np.vstack(rows)

        elif self.backend.value == "cupy":
            model.num_sim = num_sim
            for par, index in idx.items():
                vals = theta_np[:, index]
                if par in nodewise:
                    value = np.tile(vals, (nn, 1))
                    setattr(model, par, value)
                    print(f"{par}: {value}")
                else:
                    setattr(model, par, vals)
                    print(f"{par}: {vals}")
            data = model.run()
            ts = data[x]
            if ts.ndim != 3:
                raise ValueError(f"{self.backend.value} expected x=(time, nodes, nsim); got {ts.shape}")
            ts = ts.transpose(2, 1, 0)
            #TODO: extract_features has multiple kwargs available, should expose all of them as InArgs
            # or provide a single "extract_kwargs" dict?
            #TODO: Should we support selecting extract_features_df() / extract_features_list() or keep only the default
            # function?
            stat_vec = vbi.extract_features(ts=ts, cfg=self.cfg.value, fs=fs,
                                      n_workers=int(self.num_workers.value),
                                      verbose=False).values
            x = stat_vec  # (N, F)
        else:
            raise ValueError(f"{self.backend.value} backend not supported.")

        self.stat_vec.value = x
        print(f"Extracted features: {self.stat_vec.value}")

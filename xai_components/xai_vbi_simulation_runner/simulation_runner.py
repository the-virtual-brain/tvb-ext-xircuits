from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from multiprocessing import Pool
from copy import deepcopy

@xai_component(color='rgb(220, 5, 45)')
class SimulationRunner(Component):
    backend: InArg[str]
    model: InArg[any]               # union between vbi models - there is no base class
    theta: InArg[torch.Tensor]
    theta_names: InArg[list]
    cfg: InArg[dict]
    num_workers: InArg[int]

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

        fs = 1000.0 / float(self.model.value.dt)   #TODO should we expose 'fs' as a parameter?

        # infer nn for broadcasting
        nn = int(np.asarray(self.model.value.weights).shape[0])
        nodewise = {"C0", "C1", "C2", "C3"}        #TODO do we need to add more params here?

        model = self.model.value

        if self.backend.value == "cpp":
            base = model._par

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
                ts = data["x"]
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
                    setattr(model, par, np.tile(vals, (nn, 1)))  #TODO how do we want to populate these parameters?
                else:
                    setattr(model, par, vals)
            data = model.run()
            ts = data["x"]
            if ts.ndim != 3:
                raise ValueError(f"{self.backend.value} expected x=(time, nodes, nsim); got {ts.shape}")
            ts = ts.transpose(2, 1, 0)
            #TODO: extract_features has multiple kwargs available - add all of them?
            #TODO: multiple extract_features functions - do we want to expose a parameter for user to choose?
            stat_vec = vbi.extract_features(ts=ts, cfg=self.cfg.value, fs=fs,
                                      n_workers=int(self.num_workers.value),
                                      verbose=False).values
            x = stat_vec  # (N, F)
        else:
            raise ValueError(f"{self.backend.value} backend not supported.")

        self.stat_vec.value = x
        print(f"Extracted features: {self.stat_vec.value}")

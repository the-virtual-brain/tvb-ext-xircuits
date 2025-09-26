from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from multiprocessing import Pool
from copy import deepcopy

@xai_component(color='rgb(220, 5, 45)')
class BatchRun(Component):
    backend: InArg[str]          # 'cpp' or 'cupy'
    par: InArg[dict]             # base params
    theta: InArg[torch.Tensor]   # (num_sim, num_params)
    theta_names: InArg[list]
    cfg: InArg[dict]
    n_workers: InArg[int]

    stat_vec: OutArg[np.ndarray]  # (N, F)

    def execute(self, ctx):
        import vbi
        from vbi.models.cpp.jansen_rit import JR_sde as JR_cpp
        from vbi.models.cupy.jansen_rit import JR_sde as JR_cupy

        # theta -> numpy
        th = self.theta.value
        theta_np = th.detach().cpu().numpy() if hasattr(th, "detach") else np.asarray(th)
        theta_np = theta_np.astype(float, copy=False)
        num_sim, num_params = theta_np.shape

        if num_params != len(self.theta_names.value):
            raise ValueError(f"Theta has {num_params} columns, but theta_names has {len(self.theta_names.value)}.")
        idx = {n: i for i, n in enumerate(self.theta_names.value)}

        fs = 1000.0 / float(self.par.value["dt"])
        backend = (self.backend.value or "cpp").lower()

        # infer nn for broadcasting
        nn = int(np.asarray(self.par.value["weights"]).shape[0])
        nodewise = {"C0", "C1", "C2", "C3"}

        if backend == "cpp":
            base = self.par.value

            def one(sim_i: int):
                par_i = deepcopy(base)
                for col, par in idx.items():
                    val = theta_np[sim_i, par]
                    if col in nodewise:
                        par_i[par] = np.full(nn, val, dtype=float)
                    else:
                        par_i[par] = val
                data = JR_cpp(par_i).run()
                ts = data["x"]
                stat_vec = vbi.extract_features(ts=[ts], cfg=self.cfg.value, fs=fs,
                                          n_workers=1, verbose=False).values
                return stat_vec[0]

            nprocs = self.n_workers.value or 1
            with Pool(processes=nprocs) as pool:
                rows = pool.map(one, range(num_sim))

            x = np.vstack(rows)

        elif backend == "cupy":
            par1 = deepcopy(self.par.value)
            par1["num_sim"] = num_sim
            for par, index in idx.items():
                vals = theta_np[:, index]
                if par in nodewise:
                    par1[par] = np.tile(vals, (nn, 1))
                else:
                    par1[par] = vals
            data = JR_cupy(par1).run()
            ts = data["x"]
            if ts.ndim != 3:
                raise ValueError(f"CuPy expected x=(time, nodes, nsim); got {ts.shape}")
            ts = ts.transpose(2, 1, 0)
            stat_vec = vbi.extract_features(ts=ts, cfg=self.cfg.value, fs=fs,
                                      n_workers=int(self.n_workers.value or 1),
                                      verbose=False).values
            x = stat_vec  # (N, F)
        else:
            raise ValueError("backend must be 'cpp' or 'cupy'")

        self.stat_vec.value = x

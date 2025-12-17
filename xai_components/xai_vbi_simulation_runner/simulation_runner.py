from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from multiprocessing import Pool
from copy import deepcopy
from typing import Literal
from xai_components.settings import memory, OUTPUT_DIR
import os
import json


def cpp_worker(task):
    from vbi import extract_features

    (model_cls, base, theta_row, idx, nodewise, nn, fs, cfg, ts_key) = task
    par_i = deepcopy(base)
    print(theta_row, idx, nodewise, nn, fs, cfg, ts_key)
    for name, col in idx.items():
        val = theta_row[col]
        if name in nodewise:
            par_i[name] = np.full(nn, val, dtype=float)
        else:
            par_i[name] = val
    par_i.pop("dim", None)
    print("Parameters of i: ", par_i)
    data = model_cls(par_i).run()
    ts = data[ts_key]
    stat_vec = extract_features(ts=[ts], cfg=cfg, fs=fs,
                              n_workers=1, verbose=False).values
    return stat_vec[0]

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
        # theta -> numpy
        th = self.theta.value
        theta_np = th.detach().cpu().numpy() if hasattr(th, "detach") else np.asarray(th)
        theta_np = theta_np.astype(float, copy=False)
        num_sim, num_params = theta_np.shape

        if num_params != len(self.theta_names.value):
            raise ValueError(f"Theta has {num_params} columns, but theta_names has {len(self.theta_names.value)}.")
        idx = {par: index for index, par in enumerate(self.theta_names.value)}

        fs = 1000.0 / float(self.model.value.dt)

        # infer nn for broadcasting
        nn = int(np.asarray(self.model.value.weights).shape[0])

        nodewise = {"C0", "C1", "C2", "C3"}  # temporary

        model = self.model.value
        ts_key = self.time_series_key.value

        if self.backend.value == "cpp":
            model_cls = model.__class__
            base = model._par  # temporary

            tasks = []
            for i in range(num_sim):
                tasks.append((
                    model_cls,
                    base,
                    theta_np[i, :],  # row for this sim
                    idx,
                    nodewise,
                    nn,
                    fs,
                    self.cfg.value,
                    ts_key
                ))

            with Pool(processes=self.num_workers.value) as pool:
                rows = pool.map(cpp_worker, tasks)

            x = np.vstack(rows)

        elif self.backend.value == "cupy":
            resolved_par = deepcopy(model._par)
            resolved_par["num_sim"] = num_sim

            resolved_par["weights"] = np.array(resolved_par.get("weights"))

            for par, index in idx.items():
                vals = theta_np[:, index]
                if par in nodewise:
                    resolved_par[par] = np.tile(vals, (nn, 1))
                else:
                    resolved_par[par] = vals

            model_cls = model.__class__
            data = simulate_cache(model_cls, resolved_par)

            ts = data[ts_key]
            if ts.ndim != 3:
                raise ValueError(f"{self.backend.value} expected x=(time, nodes, nsim); got {ts.shape}")
            ts = ts.transpose(2, 1, 0)
            stat_vec = featurize_cache(ts, self.cfg.value, fs, int(self.num_workers.value), False)
            x = stat_vec  # (N, F)
        else:
            raise ValueError(f"{self.backend.value} backend not supported.")

        self.stat_vec.value = x

        # Store names of the inferred parameters for plotting
        path = os.path.join(OUTPUT_DIR, "priors.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["theta_names"] = self.theta_names.value
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        print(f"Extracted features: {self.stat_vec.value}")


@memory.cache
def simulate_cache(model_class, resolved_par: dict) -> dict:
    """
        Cache the simulation results.
        The cache key includes the model class and the model parameters
    """
    print(f"Resolved params: {resolved_par}")
    model = model_class(resolved_par)
    return model.run()

@memory.cache(ignore=['n_workers', 'verbose'])
def featurize_cache(ts, cfg: dict, fs: float, n_workers: int, verbose: bool) -> np.ndarray:
    """
        Cache the extracted features result.
        The cache key includes the timeseries data, feature configuration dict (cfg) and sampling frequency (fs)
    """
    from vbi import extract_features

    res = extract_features(ts=ts, cfg=cfg, fs=fs, n_workers=n_workers, verbose=verbose)
    return res.values

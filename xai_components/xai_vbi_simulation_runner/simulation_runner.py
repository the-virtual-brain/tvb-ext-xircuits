from xai_components.base import xai_component, InArg, OutArg
import numpy as np
import torch
from multiprocessing import Pool
from copy import deepcopy
from typing import Literal
from xai_components.serialization import save_params_npz
from xai_components.settings import memory
import os
import json
from xai_components.base_tvb import ComponentWithViewer


def cpp_worker(task):
    from vbi import extract_features_df

    (model_cls, base, theta_row, idx, nodewise, nn, fs, cfg, ts_key, t_key, return_data) = task
    par_i = deepcopy(base)
    for name, col in idx.items():
        val = theta_row[col]
        if name in nodewise:
            par_i[name] = np.full(nn, val, dtype=float)
        else:
            par_i[name] = val
    par_i.pop("dim", None)
    data = model_cls(par_i).run()
    ts = data[ts_key]
    stat_vec = extract_features_df(ts=[ts], cfg=cfg, fs=fs,
                              n_workers=1, verbose=False).values

    if return_data:
        return stat_vec[0], data[t_key], data[ts_key]
    else:
        return stat_vec[0], None, None

@xai_component(color='rgb(220, 5, 45)')
class SimulationRunner(ComponentWithViewer):
    backend: InArg[Literal['cupy', 'cpp', 'numba']]
    model: InArg[any]               # union between vbi models
    theta: InArg[torch.Tensor]
    theta_names: InArg[list]
    cfg: InArg[dict]
    num_workers: InArg[int]
    time_series_key: InArg[dict]
    output_dir: InArg[str]

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
        ts_key = self.time_series_key.value['x']
        t_key = self.time_series_key.value['t']

        model_cls = model.__class__
        base_par = deepcopy(model._par) # temporary
        base_par["weights"] = np.array(base_par.get("weights"), dtype=np.float64)

        if self.backend.value in ("cpp", "numba"):
            tasks = []
            for i in range(num_sim):
                tasks.append((
                    model_cls,
                    base_par,
                    theta_np[i, :],  # row for this sim
                    idx,
                    nodewise,
                    nn,
                    fs,
                    self.cfg.value,
                    ts_key, t_key,
                    i == 0
                ))

            with Pool(processes=self.num_workers.value) as pool:
                results = pool.map(cpp_worker, tasks)

            x = np.vstack([r[0] for r in results])

            # Save data for timeseries viewer
            resolved_par = self.build_resolved_par(base_par, theta_np, idx, nodewise, nn)
            t0 = next((r[1] for r in results if r[1] is not None), None)
            x0 = next((r[2] for r in results if r[2] is not None), None)

            data = {ts_key: x0, t_key: t0}

        elif self.backend.value == "cupy":
            base_par["num_sim"] = num_sim

            resolved_par = self.build_resolved_par(base_par, theta_np, idx, nodewise, nn)

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

        self.persists_artifacts(self.output_dir.value, resolved_par, data, t_key, ts_key, self.theta_names.value)
        print(f"Extracted features: {self.stat_vec.value}")

    @staticmethod
    def build_resolved_par(base_par, theta_np, idx, nodewise, nn):
        for par, index in idx.items():
            vals = theta_np[:, index]
            if par in nodewise:
                base_par[par] = np.tile(vals, (nn, 1))
            else:
                base_par[par] = vals

        return base_par

    @staticmethod
    def persists_artifacts(output_dir, resolved_par, data, t_key, ts_key, theta_names):
        # 1) model params
        params_path = os.path.join(output_dir, "model_params.npz")
        save_params_npz(resolved_par, params_path)

        # 2) simulation data
        data_path = os.path.join(output_dir, "simulation_data.npz")
        np.savez(data_path, t=data[t_key], x=data[ts_key])

        # 3) priors metadata
        path = os.path.join(output_dir, "priors.json")
        with open(path, "r", encoding="utf-8") as f:
            priors_data = json.load(f)

        priors_data["theta_names"] = theta_names
        with open(path, "w", encoding="utf-8") as f:
            json.dump(priors_data, f)


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

from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
import sbi.utils as utils

@xai_component(color="rgb(220, 5, 45)")
class TrainPosterior(Component):
    prior: InArg[utils.BoxUniform]
    theta: InArg[torch.Tensor]
    stat_vec: InArg[np.ndarray]
    method: InArg[str]
    device: InArg[str]
    density_estimator: InArg[str]
    with_mean: InArg[bool]
    with_std: InArg[bool]

    posterior: OutArg[object]
    X_scaled: OutArg[torch.Tensor]

    def __init__(self):
        super().__init__()
        self.with_mean.value = True
        self.with_std.value = True
        self.method.value = "SNPE"
        self.device.value = "cpu"
        self.density_estimator.value = "maf"

    def execute(self, ctx):
        from vbi.sbi_inference import Inference
        
        stat_vec_np = np.array(self.stat_vec.value)

        scaler = StandardScaler(
            with_mean=self.with_mean.value,
            with_std=self.with_std.value
        )
        stat_vec_st  = scaler.fit_transform(stat_vec_np)
        stat_vec_st  = torch.tensor(stat_vec_st , dtype=torch.float32)

        # Train posterior
        obj = Inference()
        posterior = obj.train(self.theta.value, stat_vec_st, self.prior.value,
                              method=self.method.value, device=self.device.value,
                              density_estimator=self.density_estimator.value)

        self.posterior.value = posterior
        self.X_scaled.value = stat_vec_st


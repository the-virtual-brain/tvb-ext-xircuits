from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
import sbi.utils as utils
from vbi.inference import Inference

@xai_component(color="rgb(220, 5, 45)")
class TrainPosterior(Component):
    inference_obj: InArg[Inference]
    theta: InArg[torch.Tensor]
    X: InArg[np.ndarray]                        # OutArg from BatchRun
    prior: InArg[utils.BoxUniform]
    method: InArg[str]            # e.g. 'SNPE'
    density_estimator: InArg[str] # e.g. 'maf'
    with_mean: InArg[bool]        # default True
    with_std: InArg[bool]         # default True

    posterior: OutArg[object]
    scaler: OutArg[StandardScaler]
    X_scaled: OutArg[torch.Tensor]

    def execute(self, ctx):
        stat_vec = np.array(self.X.value)

        scaler = StandardScaler(
            with_mean=self.with_mean.value,
            with_std=self.with_std.value
        )
        stat_vec_st  = scaler.fit_transform(stat_vec)
        stat_vec_st  = torch.tensor(stat_vec_st , dtype=torch.float32)

        # Train posterior
        method = self.method.value or "SNPE"
        density_est = self.density_estimator.value or "maf"
        posterior = self.inference_obj.value.train(self.theta.value, stat_vec_st, self.prior.value,
                              method=method, density_estimator=density_est) #TODO there are multiple fields for train function

        self.posterior.value = posterior
        self.scaler.value = scaler
        self.X_scaled.value = stat_vec_st


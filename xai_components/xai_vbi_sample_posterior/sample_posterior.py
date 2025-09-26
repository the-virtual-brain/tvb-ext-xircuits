from xai_components.base import xai_component, Component, InArg, OutArg
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
from vbi.inference import Inference

@xai_component(color="rgb(220, 5, 45)")
class SamplePosterior(Component):
    posterior: InArg[any]
    scaler: InArg[StandardScaler]
    X_scaled: InArg[any]
    num_samples: InArg[int]

    samples: OutArg[torch.Tensor]

    def execute(self, ctx):

        x_np = np.array(self.X_scaled.value)

        # ensure 2D for scaler, then transform with the SAME scaler
        if x_np.ndim == 1:
            x_np = x_np.reshape(1, -1)
        xs_np = self.scaler.value.transform(x_np).astype(np.float32, copy=False)
        xs = torch.tensor(xs_np, dtype=torch.float32)  # shape (B,F)

        # Sample Posterior
        obj = Inference()
        samples = obj.sample_posterior(xs[0, :], self.num_samples.value, self.posterior.value)
        self.samples.value = samples


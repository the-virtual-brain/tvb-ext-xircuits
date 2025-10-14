from xai_components.base import xai_component, Component, InArg, OutArg
import torch
from vbi.inference import Inference

@xai_component(color="rgb(220, 5, 45)")
class SamplePosterior(Component):
    posterior: InArg[any]
    X_scaled: InArg[any]
    num_samples: InArg[int]
    obs_idx: InArg[int]

    samples: OutArg[torch.Tensor]

    def __init__(self):
        super().__init__()
        self.obs_idx.value = 0

    def execute(self, ctx):

        x_idx_st = self.X_scaled.value[self.obs_idx.value,:]

        # Sample Posterior
        obj = Inference()
        samples = obj.sample_posterior(x_idx_st, self.num_samples.value, self.posterior.value)
        self.samples.value = samples


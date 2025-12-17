from xai_components.base import xai_component, InArg, OutArg
import torch
from vbi.sbi_inference import Inference
import os
from xai_components.settings import OUTPUT_DIR
from xai_components.base_tvb import ComponentWithViewer


@xai_component(color="rgb(220, 5, 45)")
class SamplePosterior(ComponentWithViewer):
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

        # Store the resulted samples for plotting
        path = os.path.join(OUTPUT_DIR, "samples.pt")
        torch.save(samples, path)

        self.samples.value = samples

        print(f"Sample Posterior: {self.samples.value}")
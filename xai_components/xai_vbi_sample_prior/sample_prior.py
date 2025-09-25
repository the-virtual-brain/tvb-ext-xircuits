from xai_components.base import xai_component, Component, InArg, OutArg
import torch
import sbi.utils as utils

@xai_component(color='rgb(220, 5, 45)')
class SamplePrior(Component):
    prior: InArg[utils.BoxUniform]
    num_sim: InArg[int]
    seed: InArg[int]  #optional

    theta: OutArg[torch.Tensor]
    inference_obj: OutArg[any]

    def execute(self, ctx):
        from vbi.inference import Inference

        obj = Inference()
        seed = None if self.seed.value in (None, "") else int(self.seed.value)
        self.theta.value = obj.sample_prior(self.prior.value, int(self.num_sim.value), seed)
        self.inference_obj.value = obj

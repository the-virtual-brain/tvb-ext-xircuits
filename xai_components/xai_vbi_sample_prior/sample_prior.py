from xai_components.base import xai_component, Component, InArg, OutArg
import torch
import sbi.utils as utils

@xai_component(color='rgb(220, 5, 45)')
class SamplePrior(Component):
    prior: InArg[utils.BoxUniform]
    num_sim: InArg[int]
    seed: InArg[int]

    theta: OutArg[torch.Tensor]

    def __init__(self):
        super().__init__()
        self.seed.value = None

    def execute(self, ctx):
        from vbi.inference import Inference

        obj = Inference()
        self.theta.value = obj.sample_prior(self.prior.value, int(self.num_sim.value), self.seed.value)

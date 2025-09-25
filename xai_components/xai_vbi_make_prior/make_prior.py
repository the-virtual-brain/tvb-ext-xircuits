from xai_components.base import xai_component, Component, InArg, OutArg
import torch
import sbi.utils as utils

@xai_component(color='rgb(220, 5, 45)')
class MakePrior(Component):
    prior_min: InArg[list]
    prior_max: InArg[list]

    prior: OutArg[utils.BoxUniform]

    def execute(self, ctx):
        self.prior.value = utils.BoxUniform(low=torch.tensor(self.prior_min.value),
                         high=torch.tensor(self.prior_max.value))
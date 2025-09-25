from xai_components.base import xai_component, Component, InArg, OutArg
import sbi.utils as utils
import torch

@xai_component(color='rgb(220, 5, 45)')
class ConfigInference(Component):
    prior_min: InArg[list]
    prior_max: InArg[list]
    num_sim: InArg[int]
    seed: InArg[int]  #optional
    domain_cfg: InArg[list]
    names_cfg: InArg[list]
    json_path_cfg: InArg[str]

    prior: OutArg[utils.BoxUniform]
    theta:OutArg[torch.Tensor]
    cfg: OutArg[any]
    inference_obj: OutArg[any]

    def execute(self, ctx):
        from vbi import get_features_by_domain, get_features_by_given_names
        from vbi.inference import Inference

        # Make prior
        self.prior.value = utils.BoxUniform(low=torch.tensor(self.prior_min.value),
                                            high=torch.tensor(self.prior_max.value))

        # Sample Prior
        obj = Inference()
        seed = None if self.seed.value in (None, "") else int(self.seed.value)
        self.theta.value = obj.sample_prior(self.prior.value, int(self.num_sim.value), seed)
        self.inference_obj.value = obj

        # Feature Config
        names = None if self.names_cfg in (None, "") else self.names_cfg.value
        cfg = get_features_by_domain(domain=self.domain_cfg.value, json_path=self.json_path_cfg.value)
        if names:
            cfg = get_features_by_given_names(cfg, names=names)
        self.cfg.value = cfg

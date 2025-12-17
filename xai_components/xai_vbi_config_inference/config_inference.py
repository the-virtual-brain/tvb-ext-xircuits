from xai_components.base import xai_component, Component, InArg, OutArg
import sbi.utils as utils
import torch
import os
from xai_components.settings import OUTPUT_DIR
import json

@xai_component(color='rgb(220, 5, 45)')
class ConfigInference(Component):
    prior_min: InArg[list]
    prior_max: InArg[list]
    num_sim: InArg[int]
    seed: InArg[int]
    domain_cfg: InArg[list]
    names_cfg: InArg[list]
    json_path_cfg: InArg[str]

    prior: OutArg[utils.BoxUniform]
    theta:OutArg[torch.Tensor]
    cfg: OutArg[dict]

    def __init__(self):
        super().__init__()
        self.num_sim.value = 1
        self.seed.value = None
        self.domain_cfg.value = None
        self.names_cfg.value = None
        self.json_path_cfg.value = None

    def execute(self, ctx):
        from vbi import get_features_by_domain, get_features_by_given_names
        from vbi.inference import Inference

        # Make prior
        self.prior.value = utils.BoxUniform(low=torch.tensor(self.prior_min.value),
                                            high=torch.tensor(self.prior_max.value))

        # Sample Prior
        obj = Inference()
        self.theta.value = obj.sample_prior(self.prior.value, int(self.num_sim.value), self.seed.value)
        print(f"Theta: {self.theta.value}")

        # Store theta and priors for plotting
        path = os.path.join(OUTPUT_DIR, "theta.pt")
        torch.save(self.theta.value, path)

        path = os.path.join(OUTPUT_DIR, "priors.json")
        data = {"prior_min": self.prior_min.value, "prior_max": self.prior_max.value}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        # Feature Config
        cfg = get_features_by_domain(domain=self.domain_cfg.value, json_path=self.json_path_cfg.value)
        cfg = get_features_by_given_names(cfg, names=self.names_cfg.value)
        self.cfg.value = cfg

from xai_components.base import xai_component, Component, InArg, OutArg
import sbi.utils as utils
import torch
import os
import json
from tvbextxircuits.utils import get_base_dir_web

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
    output_dir: InArg[str]

    def __init__(self):
        super().__init__()
        self.num_sim.value = 1
        self.seed.value = None
        self.domain_cfg.value = None
        self.names_cfg.value = None
        self.json_path_cfg.value = None

    def execute(self, ctx):
        from vbi import get_features_by_domain, get_features_by_given_names
        from vbi.sbi_inference import Inference

        args = ctx.get('args')
        is_hpc_launch = args.is_hpc_launch if args is not None else False
        xircuits_filename = args.xircuits_filename if args is not None else ''

        output_directory = create_output_dir(is_hpc_launch, xircuits_filename)

        # Make prior
        self.prior.value = utils.BoxUniform(low=torch.tensor(self.prior_min.value),
                                            high=torch.tensor(self.prior_max.value))

        # Sample Prior
        obj = Inference()
        self.theta.value = obj.sample_prior(self.prior.value, int(self.num_sim.value), self.seed.value)
        print(f"Theta: {self.theta.value}")

        # Store theta and priors for plotting
        path = os.path.join(output_directory, "theta.pt")
        torch.save(self.theta.value, path)

        path = os.path.join(output_directory, "priors.json")
        data = {"prior_min": self.prior_min.value, "prior_max": self.prior_max.value}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        # Feature Config
        cfg = get_features_by_domain(domain=self.domain_cfg.value, json_path=self.json_path_cfg.value)
        cfg = get_features_by_given_names(cfg, names=self.names_cfg.value)
        self.cfg.value = cfg
        self.output_dir.value = output_directory

def create_output_dir(is_hpc_launch: bool, xircuits_filename: str):
    if is_hpc_launch:
        output_dir = "output_hpc" + f"_{xircuits_filename}"
    else:
        base_root = os.path.join(get_base_dir_web(), "output")
        dirname = "output" + f"_{xircuits_filename}"
        output_dir = os.path.join(base_root, dirname)

    os.makedirs(output_dir, exist_ok=True)
    return output_dir
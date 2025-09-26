from xai_components.base import xai_component, Component, InArg, OutArg

@xai_component(color='rgb(220, 5, 45)')
class FeatureConfig(Component):
    domain: InArg[list]
    names: InArg[list]
    json_path: InArg[str]

    cfg: OutArg[dict]

    def execute(self, ctx):
        from vbi import get_features_by_domain, get_features_by_given_names

        names = None if self.names in (None, "") else self.names.value
        cfg = get_features_by_domain(domain=self.domain.value, json_path=self.json_path.value)
        if names:
            cfg = get_features_by_given_names(cfg, names=names)
        self.cfg.value = cfg
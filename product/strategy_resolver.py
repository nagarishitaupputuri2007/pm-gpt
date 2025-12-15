# product/strategy_resolver.py

from product.prioritization_strategy import (
    RICEStrategy,
    ICEStrategy,
    MoSCoWStrategy,
    KanoStrategy
)


class StrategyResolver:
    """
    Resolves a framework name into a concrete prioritization strategy
    and applies it to the generated features.
    """

    def resolve(self, framework_name: str, features: list[str]):
        if framework_name == "ICE":
            return ICEStrategy().prioritize(features)

        if framework_name == "MoSCoW":
            return MoSCoWStrategy().prioritize(features)

        if framework_name == "Kano":
            return KanoStrategy().prioritize(features)

        # Default → RICE
        return RICEStrategy().prioritize(features)

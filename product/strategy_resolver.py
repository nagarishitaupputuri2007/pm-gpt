from product.prioritization_strategy import (
    RICEStrategy,
    ICEStrategy,
    MoSCoWStrategy,
    KanoStrategy
)


class StrategyResolver:
    def resolve(self, framework_name: str):
        if framework_name == "ICE":
            return ICEStrategy()

        if framework_name == "MoSCoW":
            return MoSCoWStrategy()

        if framework_name == "Kano":
            return KanoStrategy()

        # Default
        return RICEStrategy()

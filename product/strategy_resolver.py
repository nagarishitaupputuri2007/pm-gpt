from product.prioritization_strategy import RICEStrategy, ICEStrategy


class StrategyResolver:
    """
    Resolves framework name to actual strategy implementation.
    """

    def resolve(self, framework_name: str):
        if framework_name == "ICE":
            return ICEStrategy()

        # Default fallback
        return RICEStrategy()

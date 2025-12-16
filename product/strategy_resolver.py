# product/strategy_resolver.py
from typing import List, Dict
from product.prioritization_strategy import (
    RICEStrategy,
    ICEStrategy,
    MoSCoWStrategy,
    KanoStrategy,
)

class StrategyResolver:
    """
    Resolves framework name to strategy implementation and applies it.
    Expected signature: resolve(self, framework_name: str, features: List[str]) -> List[dict]
    """

    def resolve(self, framework_name: str, features: List[str]) -> List[Dict]:
        name = (framework_name or "").strip().upper()

        if name == "ICE":
            strategy = ICEStrategy()
        elif name == "RICE":
            strategy = RICEStrategy()
        elif name == "MOSCOW" or name == "MOSCOW" or name == "MoSCoW":
            strategy = MoSCoWStrategy()
        elif name == "KANO":
            strategy = KanoStrategy()
        else:
            # fallback to RICE for roadmap-style prioritization
            strategy = RICEStrategy()

        scored = strategy.apply(features)
        # ensure we always return a list of dicts with 'feature' and 'score'
        normalized = []
        for item in scored:
            # if score missing, add a fallback
            if "score" not in item:
                item["score"] = 0
            normalized.append(item)
        return normalized

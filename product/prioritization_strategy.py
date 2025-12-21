from typing import List, Dict
import math


# --------------------------------------------------
# Base Strategy
# --------------------------------------------------
class BaseStrategy:
    def apply(self, features: List[str]) -> List[Dict]:
        raise NotImplementedError


# --------------------------------------------------
# RICE
# --------------------------------------------------
class RICEStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        scored = []
        for f in features:
            reach = max(1, len(f.split()))
            impact = 1 + sum(
                1 for kw in ["improve", "optimize", "fix", "reduce", "enhance"]
                if kw in f.lower()
            )
            confidence = 0.7
            effort = max(1, math.ceil(len(f) / 30))
            score = (reach * impact * confidence) / effort
            scored.append({"feature": f, "score": round(score, 3)})
        return scored


# --------------------------------------------------
# ICE
# --------------------------------------------------
class ICEStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        scored = []
        for f in features:
            impact = 1 + sum(
                1 for kw in ["improve", "optimize", "fix", "reduce", "increase", "add"]
                if kw in f.lower()
            )
            confidence = 0.6
            ease = max(1, 5 - len(f) // 40)
            score = (impact * confidence) / ease
            scored.append({"feature": f, "score": round(score, 3)})
        return scored


# --------------------------------------------------
# MoSCoW
# --------------------------------------------------
class MoSCoWStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        mapping = {"must": 100, "should": 75, "could": 50}
        scored = []

        for f in features:
            text = f.lower()
            if any(w in text for w in ["fix", "critical", "blocker", "reliabil"]):
                cat = "must"
            elif any(w in text for w in ["improve", "enhance", "optimize"]):
                cat = "should"
            else:
                cat = "could"

            scored.append({
                "feature": f,
                "score": mapping[cat],
                "moscow": cat
            })

        return scored


# --------------------------------------------------
# Kano
# --------------------------------------------------
class KanoStrategy(BaseStrategy):
    def apply(self, features: List[str]) -> List[Dict]:
        mapping = {
            "basic": 80,
            "performance": 60,
            "delighter": 40
        }
        scored = []

        for f in features:
            text = f.lower()
            if any(w in text for w in ["fix", "error", "crash", "reliabil"]):
                cat = "basic"
            elif any(w in text for w in ["optimize", "performance", "speed", "latency"]):
                cat = "performance"
            else:
                cat = "delighter"

            scored.append({
                "feature": f,
                "score": mapping[cat],
                "kano_category": cat
            })

        return scored


# --------------------------------------------------
# 🔑 MASTER CONTROLLER (THIS WAS MISSING)
# --------------------------------------------------
class PrioritizationStrategy:
    """
    Routes feature list to the correct prioritization framework.
    This is the ONLY class app.py should import.
    """

    def __init__(self, framework: str):
        self.framework = framework.upper()

        self.strategy_map = {
            "RICE": RICEStrategy(),
            "ICE": ICEStrategy(),
            "MOSCOW": MoSCoWStrategy(),
            "KANO": KanoStrategy()
        }

    def prioritize(self, features: List[str]) -> List[Dict]:
        strategy = self.strategy_map.get(self.framework)

        if not strategy:
            # Safe fallback
            return [{"feature": f, "score": 0} for f in features]

        return strategy.apply(features)

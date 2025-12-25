# product/prioritization_strategy.py

from typing import List, Dict


class BaseStrategy:
    def apply(self, features: List[str]) -> List[Dict]:
        raise NotImplementedError


class RICEStrategy(BaseStrategy):
    """
    PM-grade RICE scoring with explicit assumptions.
    Scores are intentionally bounded and explainable.
    """

    def apply(self, features: List[str]) -> List[Dict]:
        scored = []

        for feature in features:
            name = feature.lower()

            # ---- Reach (how many users affected)
            if "onboarding" in name or "kyc" in name:
                reach = 5
            else:
                reach = 3

            # ---- Impact (effect on first transaction completion)
            if "retry" in name or "reduce" in name or "first" in name:
                impact = 5
            elif "guide" in name or "status" in name:
                impact = 4
            else:
                impact = 3

            # ---- Confidence (how certain we are it will work)
            if "explanation" in name or "status" in name:
                confidence = 4
            else:
                confidence = 3

            # ---- Effort (engineering + compliance complexity)
            if "redesign" in name:
                effort = 5
            elif "automated" in name:
                effort = 4
            else:
                effort = 3

            score = round((reach * impact * confidence) / effort, 2)

            scored.append({
                "feature": feature,
                "score": score
            })

        return scored


class ICEStrategy(BaseStrategy):
    """
    Lightweight prioritization for fast decisions.
    """

    def apply(self, features: List[str]) -> List[Dict]:
        scored = []

        for feature in features:
            name = feature.lower()

            impact = 4 if "onboarding" in name else 3
            confidence = 3
            effort = 3 if "redesign" not in name else 4

            score = round((impact * confidence) / effort, 2)

            scored.append({
                "feature": feature,
                "score": score
            })

        return scored


class MoSCoWStrategy(BaseStrategy):
    """
    Requirement classification — converted to scores for UI compatibility.
    """

    def apply(self, features: List[str]) -> List[Dict]:
        scored = []

        for i, feature in enumerate(features):
            if i < 3:
                score = 5  # Must-have
            elif i < 6:
                score = 3  # Should-have
            else:
                score = 1  # Could-have

            scored.append({
                "feature": feature,
                "score": score
            })

        return scored


class KanoStrategy(BaseStrategy):
    """
    Simplified Kano mapping.
    """

    def apply(self, features: List[str]) -> List[Dict]:
        scored = []

        for feature in features:
            name = feature.lower()

            if "retry" in name or "reduce" in name:
                score = 5  # Performance need
            elif "guide" in name or "checklist" in name:
                score = 4  # Delighter
            else:
                score = 3  # Basic expectation

            scored.append({
                "feature": feature,
                "score": score
            })

        return scored

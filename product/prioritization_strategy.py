# product/prioritization_strategy.py

from abc import ABC, abstractmethod


class PrioritizationStrategy(ABC):
    """
    Abstract base class for all prioritization strategies.
    """

    @abstractmethod
    def prioritize(self, features: list[str]):
        pass


# --------------------------------------------------
# RICE STRATEGY
# --------------------------------------------------
class RICEStrategy(PrioritizationStrategy):
    """
    RICE = Reach × Impact × Confidence ÷ Effort
    (Simulated values for now)
    """

    def prioritize(self, features: list[str]):
        prioritized = []

        for feature in features:
            score = {
                "feature": feature,
                "RICE_score": 80  # placeholder score
            }
            prioritized.append(score)

        return prioritized


# --------------------------------------------------
# ICE STRATEGY
# --------------------------------------------------
class ICEStrategy(PrioritizationStrategy):
    """
    ICE = Impact × Confidence × Ease
    """

    def prioritize(self, features: list[str]):
        prioritized = []

        for feature in features:
            score = {
                "feature": feature,
                "ICE_score": 70  # placeholder score
            }
            prioritized.append(score)

        return prioritized


# --------------------------------------------------
# MOSCOW STRATEGY
# --------------------------------------------------
class MoSCoWStrategy(PrioritizationStrategy):
    """
    MoSCoW = Must / Should / Could / Won't
    """

    def prioritize(self, features: list[str]):
        prioritized = []

        for i, feature in enumerate(features):
            if i == 0:
                bucket = "Must Have"
            elif i == 1:
                bucket = "Should Have"
            elif i == 2:
                bucket = "Could Have"
            else:
                bucket = "Won't Have"

            prioritized.append({
                "feature": feature,
                "priority": bucket
            })

        return prioritized


# --------------------------------------------------
# KANO STRATEGY
# --------------------------------------------------
class KanoStrategy(PrioritizationStrategy):
    """
    Kano = Basic / Performance / Delighter
    """

    def prioritize(self, features: list[str]):
        prioritized = []

        for i, feature in enumerate(features):
            if i == 0:
                category = "Basic Expectation"
            elif i == 1:
                category = "Performance Feature"
            else:
                category = "Delighter"

            prioritized.append({
                "feature": feature,
                "kano_category": category
            })

        return prioritized

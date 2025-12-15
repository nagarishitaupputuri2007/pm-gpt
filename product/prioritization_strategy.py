from abc import ABC, abstractmethod


class PrioritizationStrategy(ABC):
    """
    Abstract base class for all prioritization frameworks.
    """

    @abstractmethod
    def score(self, feature: str, metrics: dict) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class RICEStrategy(PrioritizationStrategy):
    """
    RICE = (Reach × Impact × Confidence) / Effort
    """

    def name(self) -> str:
        return "RICE"

    def score(self, feature: str, metrics: dict) -> float:
        reach = metrics.get("reach", 0)
        impact = metrics.get("impact", 0)
        confidence = metrics.get("confidence", 0)
        effort = metrics.get("effort", 1)

        if effort == 0:
            effort = 1

        return (reach * impact * confidence) / effort

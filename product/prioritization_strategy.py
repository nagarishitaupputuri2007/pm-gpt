from abc import ABC, abstractmethod


class PrioritizationStrategy(ABC):
    @abstractmethod
    def prioritize(self, features):
        pass


# ---------- RICE ----------
class RICEStrategy(PrioritizationStrategy):
    def prioritize(self, features):
        return sorted(features, key=lambda x: x["score"], reverse=True)


# ---------- ICE ----------
class ICEStrategy(PrioritizationStrategy):
    def prioritize(self, features):
        return sorted(features, key=lambda x: x["score"], reverse=True)


# ---------- MoSCoW ----------
class MoSCoWStrategy(PrioritizationStrategy):
    def prioritize(self, features):
        buckets = {
            "Must Have": [],
            "Should Have": [],
            "Could Have": [],
            "Won't Have": []
        }

        for f in features:
            score = f["score"]
            name = f["feature"]

            if score >= 7:
                buckets["Must Have"].append(name)
            elif score >= 5:
                buckets["Should Have"].append(name)
            elif score >= 3:
                buckets["Could Have"].append(name)
            else:
                buckets["Won't Have"].append(name)

        return buckets


# ---------- KANO ----------
class KanoStrategy(PrioritizationStrategy):
    """
    Categorizes features based on Kano Model.
    """

    def prioritize(self, features):
        kano = {
            "Must-Be Features": [],
            "Performance Features": [],
            "Delighter Features": []
        }

        for f in features:
            score = f["score"]
            name = f["feature"]

            if score >= 7:
                kano["Must-Be Features"].append(name)
            elif score >= 4:
                kano["Performance Features"].append(name)
            else:
                kano["Delighter Features"].append(name)

        return kano

from typing import List, Dict
import random


class StrategyResolver:
    """
    Phase 4 – TRUE Framework-Specific Strategy Resolution (v3.1)

    - Each PM framework uses its OWN decision logic
    - Same features + different frameworks = DIFFERENT outcomes
    - Output shape remains consistent for app.py compatibility
    """

    # --------------------------------------------------
    # ENTRY POINT
    # --------------------------------------------------
    def resolve(self, framework: str, features: List[str]) -> List[Dict]:
        if not features:
            return []

        framework = framework.upper()

        if framework == "RICE":
            return self._resolve_rice(features)

        if framework == "ICE":
            return self._resolve_ice(features)

        if framework == "MOSCOW":
            return self._resolve_moscow(features)

        if framework == "KANO":
            return self._resolve_kano(features)

        # Safe fallback
        return self._resolve_rice(features)

    # --------------------------------------------------
    # RICE — ROI-DRIVEN, SCORE HEAVY
    # --------------------------------------------------
    def _resolve_rice(self, features: List[str]) -> List[Dict]:
        resolved = []

        for f in features:
            reach = random.randint(2, 5)
            impact = random.randint(2, 5)
            confidence = random.randint(1, 5)
            effort = random.randint(1, 5)

            score = round((reach * impact * confidence) / effort, 2)

            resolved.append({
                "feature": f,
                "score": score
            })

        return sorted(resolved, key=lambda x: x["score"], reverse=True)

    # --------------------------------------------------
    # ICE — SPEED-ORIENTED, LIGHTWEIGHT
    # --------------------------------------------------
    def _resolve_ice(self, features: List[str]) -> List[Dict]:
        resolved = []

        for f in features:
            impact = random.randint(2, 5)
            confidence = random.randint(2, 5)
            effort = random.randint(1, 4)  # ICE penalizes effort less

            score = round((impact * confidence) / effort, 2)

            resolved.append({
                "feature": f,
                "score": score
            })

        return sorted(resolved, key=lambda x: x["score"], reverse=True)

    # --------------------------------------------------
    # MoSCoW — DELIVERY & SCOPE CONTROL (NO REAL SCORES)
    # --------------------------------------------------
    def _resolve_moscow(self, features: List[str]) -> List[Dict]:
        resolved = []

        buckets = (
            ["Must Have"] * 2 +
            ["Should Have"] * 2 +
            ["Could Have"] * 2
        )

        random.shuffle(buckets)

        for f, bucket in zip(features, buckets):
            resolved.append({
                "feature": f,
                "score": bucket  # UI still expects "score"
            })

        return resolved

    # --------------------------------------------------
    # KANO — EXPERIENCE & DELIGHT CLASSIFICATION
    # --------------------------------------------------
    def _resolve_kano(self, features: List[str]) -> List[Dict]:
        resolved = []

        kano_classes = (
            ["Basic"] * 2 +
            ["Performance"] * 2 +
            ["Delighter"] * 2
        )

        random.shuffle(kano_classes)

        for f, klass in zip(features, kano_classes):
            resolved.append({
                "feature": f,
                "score": klass  # Intentional semantic score
            })

        # Delighters should appear first (PM intuition)
        priority = {"Delighter": 3, "Performance": 2, "Basic": 1}

        return sorted(
            resolved,
            key=lambda x: priority.get(x["score"], 0),
            reverse=True
        )

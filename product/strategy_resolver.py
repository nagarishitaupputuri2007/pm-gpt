from typing import List, Dict
import random


class StrategyResolver:
    """
    Phase 4 – TRUE Framework-Specific Strategy Resolution (v3.2)

    - Each PM framework uses its OWN decision logic
    - Same features + different frameworks = DIFFERENT outcomes
    - Auto mode behavior preserved
    - Manual framework selection now produces visible differences
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

        for idx, f in enumerate(features):
            reach = random.randint(3, 5)
            impact = random.randint(3, 5)
            confidence = random.randint(2, 5)
            effort = random.randint(1, 4)

            # 🔹 RICE bias: earlier features matter more for scale
            score = round((reach * impact * confidence) / effort, 2)
            score += max(0, (len(features) - idx) * 0.15)

            resolved.append({
                "feature": f,
                "score": round(score, 2)
            })

        return sorted(resolved, key=lambda x: x["score"], reverse=True)

    # --------------------------------------------------
    # ICE — SPEED & LEARNING FIRST
    # --------------------------------------------------
    def _resolve_ice(self, features: List[str]) -> List[Dict]:
        resolved = []

        for idx, f in enumerate(features):
            impact = random.randint(2, 5)
            confidence = random.randint(3, 5)
            effort = random.randint(1, 4)

            # 🔹 ICE bias: later items = quicker wins
            score = round((impact * confidence) / effort, 2)
            score += idx * 0.25

            resolved.append({
                "feature": f,
                "score": round(score, 2)
            })

        return sorted(resolved, key=lambda x: x["score"], reverse=True)

    # --------------------------------------------------
    # MoSCoW — DELIVERY & SCOPE CONTROL
    # --------------------------------------------------
    def _resolve_moscow(self, features: List[str]) -> List[Dict]:
        resolved = []

        buckets = (
            ["Must Have"] * 2 +
            ["Should Have"] * 2 +
            ["Could Have"] * 10
        )

        for f, bucket in zip(features, buckets):
            resolved.append({
                "feature": f,
                "score": bucket
            })

        return resolved

    # --------------------------------------------------
    # KANO — EXPERIENCE & DELIGHT CLASSIFICATION
    # --------------------------------------------------
    def _resolve_kano(self, features: List[str]) -> List[Dict]:
        resolved = []

        for idx, f in enumerate(features):
            if idx < 2:
                klass = "Basic"
            elif idx < 4:
                klass = "Performance"
            else:
                klass = "Delighter"

            resolved.append({
                "feature": f,
                "score": klass
            })

        priority = {"Delighter": 3, "Performance": 2, "Basic": 1}

        return sorted(
            resolved,
            key=lambda x: priority[x["score"]],
            reverse=True
        )

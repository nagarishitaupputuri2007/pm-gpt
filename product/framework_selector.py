class FrameworkSelector:
    """
    Enhanced Framework Selector (v4.3 – Balanced)

    - Prevents RICE over-dominance
    - Selects framework based on dominant PM intent
    - Requires explicit comparative signals for RICE
    """

    def select(self, problem_type: str, summary: str) -> str:
        text = summary.lower()

        framework_scores = {
            "RICE": 0,
            "ICE": 0,
            "Kano": 0,
            "MoSCoW": 0
        }

        # --------------------------------------------------
        # Problem type signals
        # --------------------------------------------------
        if problem_type in ["performance", "speed", "optimization"]:
            framework_scores["ICE"] += 3

        elif problem_type in ["onboarding", "retention", "satisfaction"]:
            framework_scores["Kano"] += 3

        elif problem_type in ["delivery", "timeline", "deadline"]:
            framework_scores["MoSCoW"] += 3

        elif problem_type in ["growth", "acquisition", "revenue"]:
            framework_scores["RICE"] += 2

        # --------------------------------------------------
        # ICE → experimentation & uncertainty
        # --------------------------------------------------
        if any(word in text for word in [
            "experiment", "test", "mvp", "hypothesis",
            "validation", "assumption", "uncertain"
        ]):
            framework_scores["ICE"] += 2

        # --------------------------------------------------
        # Kano → user emotion & expectations
        # --------------------------------------------------
        if any(word in text for word in [
            "delight", "frustration", "user satisfaction",
            "expectation", "pain point", "complaint"
        ]):
            framework_scores["Kano"] += 2

        # --------------------------------------------------
        # MoSCoW → execution & delivery
        # --------------------------------------------------
        if any(word in text for word in [
            "must have", "should have", "could have",
            "deadline", "sprint", "release", "timebox"
        ]):
            framework_scores["MoSCoW"] += 2

        # --------------------------------------------------
        # RICE → explicit comparative prioritization ONLY
        # --------------------------------------------------
        comparative_indicators = [
            "compare", "trade-off", "which should we build",
            "decide between", "rank", "prioritize between"
        ]

        scoring_indicators = [
            "reach", "impact", "confidence", "effort",
            "score", "scoring", "weighted"
        ]

        if (
            any(word in text for word in comparative_indicators)
            or all(word in text for word in ["impact", "effort"])
        ):
            framework_scores["RICE"] += 3

        # --------------------------------------------------
        # Generic prioritization (weak signal)
        # --------------------------------------------------
        if "prioritiz" in text:
            framework_scores["RICE"] += 1
            framework_scores["ICE"] += 1

        # --------------------------------------------------
        # Safe fallback
        # --------------------------------------------------
        if max(framework_scores.values()) == 0:
            return "RICE"

        # --------------------------------------------------
        # Deterministic selection
        # --------------------------------------------------
        top_score = max(framework_scores.values())
        tied = [fw for fw, s in framework_scores.items() if s == top_score]

        # Priority based on PM intent clarity
        for fw in ["ICE", "Kano", "RICE", "MoSCoW"]:
            if fw in tied:
                return fw

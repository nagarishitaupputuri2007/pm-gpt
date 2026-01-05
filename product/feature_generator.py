from typing import List


class FeatureGenerator:
    """
    Phase 4 – Context-Aware Feature Generation (v4.1)

    - Generates DIFFERENT features based on problem_type + summary
    - Uses PM mental models:
        • Funnel stage
        • Dominant business risk
    - Normalizes inputs to avoid silent fallbacks
    """

    def generate(self, problem_type: str, summary: str) -> List[str]:
        # --------------------------------------------------
        # NORMALIZE INPUTS (CRITICAL FIX)
        # --------------------------------------------------
        problem_type = (problem_type or "").lower().strip()
        text = (summary or "").lower()

        # Map real-world labels to canonical problem types
        PROBLEM_TYPE_ALIASES = {
            "activation": "onboarding",
            "signup": "onboarding",
            "kyc": "onboarding",
            "churn": "retention",
            "engagement": "retention",
            "reliability": "performance",
            "stability": "performance",
            "latency": "performance",
            "execution": "delivery",
            "shipping": "delivery",
            "nps": "satisfaction",
            "feedback": "satisfaction",
            "growth_rate": "growth",
            "conversion": "growth",
        }

        problem_type = PROBLEM_TYPE_ALIASES.get(problem_type, problem_type)

        # --------------------------------------------------
        # DERIVED PM CONTEXT (RULE-BASED, LIGHTWEIGHT)
        # --------------------------------------------------

        # Funnel stage inference
        if any(k in text for k in ["first value", "activation", "signup", "onboarding", "kyc"]):
            funnel = "activation"
        elif any(k in text for k in ["engagement", "repeat", "habit", "usage"]):
            funnel = "engagement"
        elif any(k in text for k in [
            "pricing", "upgrade", "monetization", "conversion",
            "trial", "free trial", "trial ends", "paywall"
        ]):
            funnel = "monetization"

        elif any(k in text for k in ["latency", "reliability", "downtime", "failure"]):
            funnel = "reliability"
        else:
            funnel = "general"

        # Risk inference
        if any(k in text for k in ["compliance", "regulatory", "kyc", "audit"]):
            risk = "compliance"
        elif any(k in text for k in [
            "revenue", "pricing", "upgrade", "churn",
            "trial", "trial ends", "not converting"
        ]):
            risk = "revenue"

        elif any(k in text for k in ["trust", "confidence", "credibility"]):
            risk = "trust"
        elif any(k in text for k in ["support", "cost", "operations"]):
            risk = "cost"
        else:
            risk = "speed"

        # --------------------------------------------------
        # FEATURE GENERATION (PM-REALISTIC)
        # --------------------------------------------------

        # -------- ONBOARDING --------
        if problem_type == "onboarding":

            if risk == "compliance":
                return [
                    "Introduce progressive disclosure for compliance steps instead of upfront blocking",
                    "Add real-time validation with explicit failure reasons during document upload",
                    "Provide guided retry paths instead of forcing onboarding restarts",
                    "Display verification status clearly with expected resolution timelines",
                    "Reduce non-essential data collection before first compliance checkpoint",
                ]

            return [
                "Reduce non-essential fields before the user reaches first value",
                "Introduce a progressive onboarding flow that unlocks steps only when required",
                "Display a clear progress indicator tied to first-value completion",
                "Add inline microcopy explaining why each required step exists",
                "Surface a first-success confirmation moment to reinforce completion",
            ]

        # -------- RETENTION --------
        if problem_type == "retention":

            if funnel == "monetization":
                return [
                    "Clarify feature gating with in-context previews of locked value",
                    "Surface upgrade prompts only after users experience core value",
                    "Align pricing tiers with observed usage patterns",
                    "Reduce surprise paywalls by signaling limitations earlier",
                    "Introduce time-bound upgrade nudges based on value realization",
                ]

            return [
                "Introduce early-warning signals to detect disengaging users",
                "Trigger re-engagement nudges based on drop-off behavior patterns",
                "Add habit-forming reminders tied to core value moments",
                "Personalize workflows based on prior usage behavior",
                "Create lightweight win-back flows for inactive users",
                "Replace generic notifications with lifecycle-based messaging",
            ]

        # -------- PERFORMANCE --------
        if problem_type == "performance":
            return [
                "Instrument latency and failure metrics across critical user flows",
                "Introduce graceful degradation when non-critical services fail",
                "Add user-visible system status indicators during outages",
                "Prioritize reliability improvements over feature expansion",
                "Create automated alerts tied to user-impact thresholds",
            ]

        # -------- DELIVERY --------
        if problem_type == "delivery":
            return [
                "Introduce a single-owner model for roadmap commitments",
                "Establish must-ship vs nice-to-have delivery tiers",
                "Limit work-in-progress to reduce context switching",
                "Create quarterly delivery confidence checkpoints",
                "Align roadmap planning with engineering capacity forecasts",
            ]

        # -------- SATISFACTION --------
        if problem_type == "satisfaction":
            return [
                "Collect contextual feedback immediately after key interactions",
                "Personalize workflows based on user preferences",
                "Reduce friction in commonly repeated actions",
                "Introduce delight moments in high-frequency flows",
                "Close the feedback loop by visibly acting on user input",
            ]

        # -------- GROWTH --------
        if problem_type == "growth":
            return [
                "Optimize conversion points by reducing cognitive load",
                "Introduce referral or viral loops tied to core value moments",
                "Experiment with pricing or packaging for expansion revenue",
                "Improve activation-to-conversion handoff",
                "Instrument growth experiments with clear success metrics",
            ]

        # -------- SAFE DEFAULT (ONLY WHEN INPUT IS TRULY AMBIGUOUS) --------
        return [
            "Clarify the primary user value being delivered",
            "Reduce friction in the most frequently used workflows",
            "Introduce feedback loops to validate user impact",
            "Prioritize changes tied to measurable outcomes",
        ]

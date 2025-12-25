from typing import Dict, List


class ProblemMapper:
    """
    Phase 4 – True PM Problem Generalization (v3.1)

    What’s new vs v3.0:
    - Adds problem_subtype (🔥 critical)
    - Adds dominant_goal (what PM is optimizing for)
    - Adds dominant_risk (what PM is afraid of)
    - Keeps ALL existing keys (backward compatible)
    """

    def map(self, problem_text: str) -> Dict:
        text = problem_text.lower()

        # --------------------------------------------------
        # SIGNAL GROUPS
        # --------------------------------------------------
        signals = {
            "onboarding": ["onboarding", "activation", "signup", "first-time", "kyc"],
            "retention": ["retention", "churn", "drop-off", "repeat", "engagement"],
            "performance": ["latency", "slow", "downtime", "crash", "reliability"],
            "delivery": ["delivery", "deadline", "scope", "roadmap", "planning"],
            "satisfaction": ["experience", "feedback", "usability", "delight"],
            "growth": ["growth", "revenue", "monetization", "conversion", "scale"],
        }

        def has_any(words: List[str]) -> bool:
            return any(w in text for w in words)

        # --------------------------------------------------
        # PRIMARY PROBLEM TYPE (STRICT ORDER)
        # --------------------------------------------------
        if has_any(signals["performance"]):
            problem_type = "performance"
        elif has_any(signals["delivery"]):
            problem_type = "delivery"
        elif has_any(signals["retention"]):
            problem_type = "retention"
        elif has_any(signals["onboarding"]):
            problem_type = "onboarding"
        elif has_any(signals["satisfaction"]):
            problem_type = "satisfaction"
        elif has_any(signals["growth"]):
            problem_type = "growth"
        else:
            problem_type = "general"

        # --------------------------------------------------
        # SUBTYPE (THIS IS THE DIFFERENTIATOR)
        # --------------------------------------------------
        if problem_type == "retention":
            if has_any(["pricing", "paywall", "upgrade", "subscription"]):
                problem_subtype = "pricing_retention"
            elif has_any(["habit", "frequency", "daily", "weekly"]):
                problem_subtype = "habit_retention"
            elif has_any(["content", "relevance", "personalization"]):
                problem_subtype = "value_retention"
            else:
                problem_subtype = "generic_retention"

        elif problem_type == "onboarding":
            if has_any(["kyc", "compliance", "verification"]):
                problem_subtype = "compliance_onboarding"
            elif has_any(["confusing", "unclear", "too many steps"]):
                problem_subtype = "cognitive_overload"
            else:
                problem_subtype = "activation_friction"

        elif problem_type == "growth":
            if has_any(["conversion", "funnel", "drop"]):
                problem_subtype = "conversion_growth"
            elif has_any(["pricing", "upsell", "expansion"]):
                problem_subtype = "revenue_growth"
            else:
                problem_subtype = "topline_growth"

        elif problem_type == "performance":
            problem_subtype = "system_reliability"

        elif problem_type == "delivery":
            problem_subtype = "execution_alignment"

        elif problem_type == "satisfaction":
            problem_subtype = "experience_quality"

        else:
            problem_subtype = "general"

        # --------------------------------------------------
        # DOMINANT PM GOAL (WHAT SUCCESS MEANS)
        # --------------------------------------------------
        if problem_type == "onboarding":
            dominant_goal = "activation"
        elif problem_type == "retention":
            dominant_goal = "repeat_usage"
        elif problem_type == "growth":
            dominant_goal = "revenue_or_scale"
        elif problem_type == "performance":
            dominant_goal = "reliability"
        elif problem_type == "delivery":
            dominant_goal = "predictability"
        elif problem_type == "satisfaction":
            dominant_goal = "sentiment"
        else:
            dominant_goal = "value_clarity"

        # --------------------------------------------------
        # DOMINANT PM RISK (WHAT COULD GO WRONG)
        # --------------------------------------------------
        if has_any(["compliance", "regulatory", "audit"]):
            dominant_risk = "compliance"
        elif has_any(["revenue", "pricing", "churn"]):
            dominant_risk = "revenue"
        elif has_any(["trust", "confidence", "credibility"]):
            dominant_risk = "trust"
        elif has_any(["support", "cost", "ops"]):
            dominant_risk = "cost"
        else:
            dominant_risk = "execution_speed"

        # --------------------------------------------------
        # CORE PM FRAMING
        # --------------------------------------------------
        core_problem = (
            f"The product struggles with {problem_subtype.replace('_', ' ')} "
            f"due to unresolved user friction and misaligned priorities"
        )

        user_failure_point = (
            "Users fail to consistently realize or sustain value during critical moments"
        )

        business_impact = [
            "Erosion of user trust",
            "Reduced long-term product value",
            "Increased operational burden"
        ]

        constraints = [
            "Engineering capacity is limited",
            "Business risk must be controlled",
            "Solutions must scale sustainably"
        ]

        success_definition = (
            f"Improve {dominant_goal.replace('_', ' ')} while controlling "
            f"{dominant_risk.replace('_', ' ')} risk"
        )

        summary = (
            f"The core issue is that {core_problem.lower()}. "
            f"This leads to poor {dominant_goal.replace('_', ' ')} "
            f"and exposes the business to {dominant_risk.replace('_', ' ')} risk."
        )

        # --------------------------------------------------
        # RETURN (BACKWARD + FORWARD COMPATIBLE)
        # --------------------------------------------------
        return {
            "problem_type": problem_type,
            "problem_subtype": problem_subtype,        
            "dominant_goal": dominant_goal,            
            "dominant_risk": dominant_risk,            
            "core_problem": core_problem,
            "user_failure_point": user_failure_point,
            "business_impact": business_impact,
            "constraints": constraints,
            "success_definition": success_definition,
            "summary": summary,
        }

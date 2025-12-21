from typing import Dict, List


class ProblemMapper:
    """
    Converts a raw product problem into a PM-grade problem insight.
    Focused on clarity, causality, and business defensibility.
    """

    def map(self, problem_text: str) -> Dict:
        text = problem_text.lower()

        # -----------------------------
        # Domain signals
        # -----------------------------
        fintech_signals = ["kyc", "upi", "payments", "compliance", "verification", "transaction"]
        cost_signals = ["support", "tickets", "cost", "operational"]
        trust_signals = ["trust", "confidence", "credibility"]

        def contains_any(words: List[str]) -> bool:
            return any(w in text for w in words)

        is_fintech = contains_any(fintech_signals)

        # -----------------------------
        # Core Problem (CAUSE + CONSEQUENCE)
        # -----------------------------
        if is_fintech:
            core_problem = (
                "Compliance-heavy onboarding creates friction that prevents users from "
                "completing their first successful transaction"
            )
        else:
            core_problem = (
                "Onboarding friction prevents users from reaching initial product value"
            )

        # -----------------------------
        # Critical Failure Point (USER BEHAVIOR) ✅ ULTRA-SHARP PM VERSION
        # -----------------------------
        failure_point = (
            "Users stall or abandon onboarding when required steps feel unclear or repetitive, "
            "causing perceived effort to outweigh expected value before the first transaction"
        )

        # -----------------------------
        # Business Impact
        # -----------------------------
        impacts = []

        if contains_any(cost_signals):
            impacts.append("Increased operational and support costs")

        impacts.append("Lower activation and first-transaction completion rates")

        if contains_any(trust_signals) or is_fintech:
            impacts.append("Erosion of customer trust during first use")

        # -----------------------------
        # Constraints (NON-NEGOTIABLES)
        # -----------------------------
        constraints = [
            "Compliance requirements are non-negotiable",
            "Engineering capacity is limited",
            "Support headcount cannot be increased"
        ]

        # -----------------------------
        # Success Definition (METRIC-ORIENTED)
        # -----------------------------
        if "60 days" in text or "within 60 days" in text:
            success_definition = (
                "Increase first-transaction completion rate within 60 days "
                "without increasing compliance risk or support load"
            )
        else:
            success_definition = (
                "Increase first-transaction completion rate within a fixed short-term window"
            )

        # -----------------------------
        # PM SUMMARY (EXECUTIVE-READY)
        # -----------------------------
        summary = (
            f"The core problem is that {core_problem.lower()}. "
            f"In practice, this occurs because {failure_point.lower()}. "
            f"As a result, the business faces {', '.join(i.lower() for i in impacts)}. "
            f"Any solution must operate within constraints such as "
            f"{', '.join(c.lower() for c in constraints)}."
        )

        return {
            "core_problem": core_problem,
            "user_failure_point": failure_point,
            "business_impact": impacts,
            "constraints": constraints,
            "success_definition": success_definition,
            "summary": summary
        }

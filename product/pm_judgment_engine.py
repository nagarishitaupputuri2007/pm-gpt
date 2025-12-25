from typing import List, Dict


class PMJudgmentEngine:
    """
    Generates executive-grade PM judgment.
    This module makes HARD calls and DEFENDS them.
    Deterministic, rule-based, interview-safe.
    """

    def generate(
        self,
        problem: str,
        constraints: List[str],
        prioritized_features: List[Dict],
        roadmap: Dict[str, List[str]],
    ) -> Dict[str, str]:

        top_feature = (
            prioritized_features[0]["feature"]
            if prioritized_features
            else "onboarding friction reduction"
        )

        # 1. Explicit non-decisions
        did_not_do = (
            "We explicitly avoided reducing or bypassing KYC and compliance checks. "
            "Although compliance contributes to drop-off, relaxing these requirements "
            "would introduce regulatory and trust risk that outweighs short-term activation gains."
        )

        # 2. Primary bet
        primary_bet = (
            f"The primary bet is that reducing perceived onboarding effort — particularly via "
            f"{top_feature.lower()} — will unlock first-transaction completion without increasing "
            "compliance risk or support load."
        )

        # 3. Biggest execution risk
        execution_risk = (
            "The largest execution risk is that guided retries and additional guidance increase "
            "attempt volume without improving completion if error feedback is not sufficiently clear. "
            "This would raise operational cost without improving activation."
        )

        # 4. Controversial trade-off
        tradeoff = (
            "We intentionally deprioritized new feature expansion and growth experiments to preserve "
            "engineering capacity for onboarding stabilization. This sacrifices short-term roadmap "
            "breadth in favor of fixing the highest-impact activation bottleneck."
        )

        # 5. Leadership pushback + response
        leadership_exchange = (
            "**Leadership:** Why not automate or shortcut KYC further to speed onboarding?\n\n"
            "**PM:** Given current constraints, additional automation increases false positives and "
            "re-verification loops, which erodes trust and raises support volume. Improving clarity "
            "and retry success delivers activation gains without introducing regulatory risk."
        )

        return {
            "did_not_do": did_not_do,
            "primary_bet": primary_bet,
            "execution_risk": execution_risk,
            "tradeoff": tradeoff,
            "leadership_exchange": leadership_exchange,
        }

# product/problem_mapper.py

class ProblemMapper:
    """
    Phase 3 – Smart, Real-World Problem Understanding (v2.1)

    Goals:
    - Handle messy, real PM problem statements
    - Detect multiple independent problem dimensions
    - Identify primary vs secondary issues
    - Produce senior-PM style problem diagnosis
    - No AI calls, no overfitting, fully deterministic
    """

    def map_problem(self, problems):
        text = " ".join(problems).lower()

        # --- Signal buckets with weights ---
        signal_map = {
            "activation / onboarding": {
                "keywords": ["onboarding", "sign up", "signup", "first time", "activate", "getting started"],
                "weight": 0
            },
            "retention / churn": {
                "keywords": ["churn", "drop", "drop off", "leave", "retention", "not coming back"],
                "weight": 0
            },
            "performance / reliability": {
                "keywords": ["slow", "performance", "latency", "load", "crash", "bug"],
                "weight": 0
            },
            "value clarity": {
                "keywords": ["confusing", "unclear", "value", "benefit", "understand"],
                "weight": 0
            },
            "monetization / growth": {
                "keywords": ["revenue", "monetization", "pricing", "paid", "upgrade", "growth"],
                "weight": 0
            }
        }

        # --- Detect signals ---
        for category, data in signal_map.items():
            for kw in data["keywords"]:
                if kw in text:
                    data["weight"] += 1

        # --- Keep only detected signals ---
        detected = {
            k: v["weight"]
            for k, v in signal_map.items()
            if v["weight"] > 0
        }

        if not detected:
            return (
                "The product is experiencing broad user experience and engagement challenges. "
                "The underlying drivers are unclear and require further qualitative and quantitative investigation."
            )

        # --- Rank by severity ---
        ranked = sorted(detected.items(), key=lambda x: x[1], reverse=True)

        primary = ranked[0][0]
        secondary = [r[0] for r in ranked[1:3]]

        # --- Build PM-style diagnosis ---
        diagnosis = f"The primary challenge facing the product is **{primary}**."

        if secondary:
            diagnosis += (
                " This is compounded by issues in "
                + " and ".join(f"**{s}**" for s in secondary)
                + "."
            )

        diagnosis += (
            " Together, these problems are negatively impacting user activation, "
            "retention, and overall business growth."
        )

        return diagnosis

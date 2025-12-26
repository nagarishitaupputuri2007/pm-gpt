class FrameworkSelector:
    """
    Enhanced Framework Selector (v4.1)

    - Selects the most appropriate prioritization framework
    - Uses problem type + semantic keyword analysis
    - Deterministic tie-breaking with PM rationale
    """

    def select(self, problem_type: str, summary: str) -> str:
        text = summary.lower()

        # --------------------------------------------------
        # Framework score initialization
        # --------------------------------------------------
        framework_scores = {
            "RICE": 0,
            "ICE": 0,
            "Kano": 0,
            "MoSCoW": 0
        }

        # --------------------------------------------------
        # Analyze problem type
        # --------------------------------------------------
        if problem_type in ["performance", "speed", "optimization"]:
            framework_scores["ICE"] += 3
            framework_scores["RICE"] += 1

        elif problem_type in ["delivery", "timeline", "deadline"]:
            framework_scores["MoSCoW"] += 3

        elif problem_type in ["onboarding", "retention", "satisfaction"]:
            framework_scores["Kano"] += 3
            framework_scores["RICE"] += 1

        elif problem_type in ["growth", "acquisition", "revenue"]:
            framework_scores["RICE"] += 2
            framework_scores["ICE"] += 1

        # --------------------------------------------------
        # Keyword-based semantic analysis
        # --------------------------------------------------

        # RICE → business impact & strategic planning
        rice_indicators = [
            "roi", "investment", "business impact",
            "quarterly planning", "roadmap",
            "strategic", "long-term", "growth", "revenue"
        ]
        if any(word in text for word in rice_indicators):
            framework_scores["RICE"] += 2

        # ICE → experimentation & uncertainty
        ice_indicators = [
            "quick win", "experiment", "test", "mvp",
            "validation", "hypothesis",
            "assumption", "uncertain", "exploratory"
        ]
        if any(word in text for word in ice_indicators):
            framework_scores["ICE"] += 2

        # Kano → user emotion & expectations (NO delivery terms)
        kano_indicators = [
            "user satisfaction", "delight",
            "expectation", "basic need",
            "delighter", "satisfier", "frustration"
        ]
        if any(word in text for word in kano_indicators):
            framework_scores["Kano"] += 2

        # MoSCoW → delivery, urgency & prioritization
        moscow_indicators = [
            "must have", "should have", "could have", "won't have",
            "critical", "important", "nice to have",
            "deadline", "timebox", "sprint", "release"
        ]
        if any(word in text for word in moscow_indicators):
            framework_scores["MoSCoW"] += 2

        # --------------------------------------------------
        # Special case: prioritization problems
        # --------------------------------------------------
        if "prioritiz" in text:
            framework_scores["RICE"] += 1
            framework_scores["ICE"] += 1

        # --------------------------------------------------
        # Safe fallback (no signals detected)
        # --------------------------------------------------
        if max(framework_scores.values()) == 0:
            return "RICE"  # safest default for vague problems

        # --------------------------------------------------
        # Framework selection
        # --------------------------------------------------
        selected = max(framework_scores.items(), key=lambda x: x[1])[0]

        # --------------------------------------------------
        # Tie-breaker logic
        # Priority rationale:
        # RICE > ICE > Kano > MoSCoW
        # Business impact > Experimentation > UX > Delivery
        # --------------------------------------------------
        top_score = framework_scores[selected]
        tied = [fw for fw, score in framework_scores.items() if score == top_score]

        for fw in ["RICE", "ICE", "Kano", "MoSCoW"]:
            if fw in tied:
                return fw

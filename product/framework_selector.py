class FrameworkSelector:
    """
    Enhanced Framework Selector (v4.0)
    
    - Analyzes problem context to select the most appropriate framework
    - Considers multiple factors including problem type, text content, and context
    - Provides more accurate and dynamic framework selection
    """

    def select(self, problem_type: str, summary: str) -> str:
        text = summary.lower()
        
        # Dictionary to hold framework scores
        framework_scores = {
            "RICE": 0,
            "ICE": 0,
            "Kano": 0,
            "MoSCoW": 0
        }
        
        # Analyze problem type
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

        # Analyze text content
        # RICE indicators
        rice_indicators = ["roi", "investment", "business impact", "quarterly planning", 
                         "roadmap", "strategic", "long-term", "growth", "revenue"]
        if any(indicator in text for indicator in rice_indicators):
            framework_scores["RICE"] += 2
            
        # ICE indicators
        ice_indicators = ["quick win", "experiment", "test", "mvp", "validation", 
                         "hypothesis", "assumption", "uncertain", "exploratory"]
        if any(indicator in text for indicator in ice_indicators):
            framework_scores["ICE"] += 2
            
        # Kano indicators
        kano_indicators = ["user satisfaction", "delight", "must have", "basic need", 
                          "expectation", "delighter", "satisfier", "frustration"]
        if any(indicator in text for indicator in kano_indicators):
            framework_scores["Kano"] += 2
            
        # MoSCoW indicators
        moscow_indicators = ["must have", "should have", "could have", "won't have",
                            "critical", "important", "nice to have", "not important",
                            "deadline", "timebox", "sprint", "release"]
        if any(indicator in text for indicator in moscow_indicators):
            framework_scores["MoSCoW"] += 2

        # Special case: If the problem is about prioritization itself
        if "prioritiz" in text:
            framework_scores["RICE"] += 1
            framework_scores["ICE"] += 1

        # Select framework with highest score
        selected = max(framework_scores.items(), key=lambda x: x[1])[0]
        
        # If there's a tie, use this priority order
        if list(framework_scores.values()).count(framework_scores[selected]) > 1:
            if framework_scores["RICE"] == framework_scores[selected]:
                return "RICE"
            elif framework_scores["ICE"] == framework_scores[selected]:
                return "ICE"
            elif framework_scores["Kano"] == framework_scores[selected]:
                return "Kano"
                
        return selected
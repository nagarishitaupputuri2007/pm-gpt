from typing import Dict, List
import re

class ProblemMapper:
    """
    Enhanced Problem Mapper with dynamic, context-aware responses.
    """
    
    def __init__(self):
        # Initialize any required components (e.g., NLP models, keyword extractors)
        pass
    
    def extract_key_phrases(self, text: str) -> List[str]:
        """Extract key phrases from the problem text."""
        # Simple keyword extraction (can be enhanced with NLP libraries like spaCy)
        words = re.findall(r'\b\w+\b', text.lower())
        return list(set(words))  # Remove duplicates
    
    def map(self, problem_text: str) -> Dict:
        text = problem_text.lower()
        key_phrases = self.extract_key_phrases(text)
        
        # --------------------------------------------------
        # SIGNAL GROUPS
        # --------------------------------------------------
        signals = {
            "onboarding": ["onboarding", "signup", "activation", "first-time", "kyc"],
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
        # DYNAMIC RESPONSES
        # --------------------------------------------------
        # 1. Core Problem
        problem_templates = {
            "onboarding": f"The onboarding process is hindered by {self._describe_issue(text, 'complexity', 'unclear steps')}, causing users to abandon the process.",
            "retention": f"Users are churning due to {self._describe_issue(text, 'lack of value', 'poor experience')} in the {self._extract_feature(text) or 'product'}.",
            "performance": f"The product suffers from {self._describe_issue(text, 'performance issues', 'slow response times')}, particularly in the {self._extract_feature(text) or 'critical path'}.",
            "delivery": f"The team is struggling with {self._describe_issue(text, 'delivery challenges', 'unclear priorities')} for the {self._extract_feature(text) or 'upcoming release'}.",
            "satisfaction": f"User satisfaction is impacted by {self._describe_issue(text, 'usability issues', 'missing features')} in the {self._extract_feature(text) or 'user journey'}.",
            "growth": f"Business growth is limited by {self._describe_issue(text, 'conversion barriers', 'market challenges')} in the {self._extract_feature(text) or 'customer acquisition funnel'}.",
            "general": f"The product faces challenges with {self._describe_issue(text, 'user needs', 'technical constraints')} that need to be addressed."
        }
        core_problem = problem_templates.get(problem_type, problem_templates["general"])
        
        # 2. User Failure Point
        failure_templates = {
            "onboarding": f"Users drop off at the {self._extract_step(text) or 'registration'} step because {self._describe_issue(text, 'it is too complex', 'they encounter errors')}.",
            "retention": f"Users stop engaging after {self._extract_timeframe(text) or 'a short period'} due to {self._describe_issue(text, 'lack of value', 'poor experience')}.",
            "performance": f"Users experience {self._describe_issue(text, 'slow performance', 'frequent crashes')} when {self._extract_action(text) or 'using key features'}.",
            "delivery": f"The team misses deadlines because {self._describe_issue(text, 'of scope creep', 'unrealistic timelines')} for the {self._extract_feature(text) or 'project'}.",
            "satisfaction": f"Users report frustration with {self._describe_issue(text, 'the interface', 'missing functionality')} in the {self._extract_feature(text) or 'product'}.",
            "growth": f"Growth is stunted by {self._describe_issue(text, 'low conversion rates', 'high churn')} in the {self._extract_funnel_stage(text) or 'customer journey'}.",
            "general": f"Users struggle with {self._describe_issue(text, 'the product', 'key features')} due to {self._extract_issue(text) or 'unresolved issues'}."
        }
        user_failure_point = failure_templates.get(problem_type, failure_templates["general"])
        
        # 3. Business Impact
        impact_templates = {
            "onboarding": [
                f"High drop-off rates ({self._extract_metric(text, 'drop-off rate') or 'significant'}) during signup",
                f"Low activation rates ({self._extract_metric(text, 'activation rate') or 'below target'})",
                f"Increased support costs due to {self._describe_issue(text, 'user confusion', 'technical issues')}"
            ],
            "retention": [
                f"High churn rate of {self._extract_metric(text, 'churn rate') or 'alarming levels'}",
                f"Reduced customer lifetime value by {self._extract_metric(text, 'LTV') or 'a significant margin'}",
                f"Negative word-of-mouth affecting {self._extract_metric(text, 'NPS') or 'brand reputation'}"
            ],
            # ... (similar templates for other problem types)
        }
        business_impact = impact_templates.get(problem_type, [
            "Erosion of user trust",
            "Reduced long-term product value",
            "Increased operational burden"
        ])
        
        # 4. Constraints
        constraints_map = {
            "onboarding": [
                f"Limited {self._extract_resource(text) or 'engineering'} resources for improvements",
                f"Need to balance {self._extract_tradeoff(text) or 'security with usability'}"
            ],
            "retention": [
                f"Limited {self._extract_resource(text) or 'user behavior'} data",
                f"Need for quick wins to show {self._extract_metric(text, 'improvement') or 'progress'}"
            ],
            # ... (similar templates for other problem types)
        }
        constraints = constraints_map.get(problem_type, [
            "Engineering capacity is limited",
            "Business risk must be controlled",
            "Solutions must scale sustainably"
        ])
        
        # 5. Success Definition
        success_definition = (
            f"Improve {self._extract_goal(text) or dominant_goal.replace('_', ' ')} by "
            f"{self._extract_metric(text, 'target') or 'a significant margin'} "
            f"while controlling {self._extract_risk(text) or dominant_risk.replace('_', ' ')} risks."
        )

        # 6. Summary
        summary = (
            f"The core issue is {core_problem.lower()} "
            f"This impacts {self._extract_stakeholder(text) or 'users'} by {user_failure_point.lower()} "
            f"Addressing this could lead to improvements in {self._extract_benefit(text) or 'user satisfaction and business outcomes'}."
        )

        return {
            "problem_type": problem_type,
            "problem_subtype": problem_type,  # Can be enhanced with more specific subtypes
            "dominant_goal": self._extract_goal(text) or dominant_goal,
            "dominant_risk": self._extract_risk(text) or dominant_risk,
            "core_problem": core_problem,
            "user_failure_point": user_failure_point,
            "business_impact": business_impact,
            "constraints": constraints,
            "success_definition": success_definition,
            "summary": summary,
            "key_phrases": key_phrases  # For debugging and further analysis
        }
    
    # Helper methods for dynamic text generation
    def _extract_feature(self, text: str) -> str:
        """Extract a feature or component mentioned in the text."""
        # Simple implementation - can be enhanced with NLP
        features = ["dashboard", "checkout", "search", "api", "mobile app", "web app"]
        for feature in features:
            if feature in text:
                return feature
        return ""
    
    def _extract_metric(self, text: str, metric_type: str) -> str:
        """Extract a metric value from the text."""
        # Simple implementation - can be enhanced with regex or NLP
        metrics = {
            "drop-off rate": ["% drop-off", "drop off rate"],
            "activation rate": ["% activation", "activation rate"],
            "churn rate": ["% churn", "churn rate"],
            "LTV": ["LTV", "lifetime value"],
            "NPS": ["NPS", "net promoter score"]
        }
        for m in metrics.get(metric_type, []):
            if m in text:
                # Extract the number before the metric if available
                numbers = re.findall(r'(\d+)\s*' + re.escape(m), text)
                if numbers:
                    return f"{numbers[0]}%"
        return ""
    
    def _describe_issue(self, text: str, default: str, alternative: str) -> str:
        """Choose a description based on what's mentioned in the text."""
        return default if any(w in text for w in default.split()) else alternative
    
    def _extract_step(self, text: str) -> str:
        """Extract a step in a process from the text."""
        steps = ["signup", "registration", "verification", "onboarding", "checkout"]
        return next((step for step in steps if step in text), "")
    
    def _extract_timeframe(self, text: str) -> str:
        """Extract a timeframe from the text."""
        timeframes = ["a few days", "a week", "a month", "the first use"]
        return next((tf for tf in timeframes if tf in text), "a short period")
    
    def _extract_action(self, text: str) -> str:
        """Extract an action from the text."""
        actions = ["clicking", "submitting", "loading", "navigating", "searching"]
        return next((f"{action} {self._extract_feature(text) or 'the page'}" 
                    for action in actions if action in text), "")
    
    def _extract_funnel_stage(self, text: str) -> str:
        """Extract a funnel stage from the text."""
        stages = ["awareness", "consideration", "conversion", "retention", "referral"]
        return next((stage for stage in stages if stage in text), "customer journey")
    
    def _extract_resource(self, text: str) -> str:
        """Extract a resource constraint from the text."""
        resources = ["engineering", "design", "budget", "time", "team"]
        return next((res for res in resources if res in text), "")
    
    def _extract_tradeoff(self, text: str) -> str:
        """Extract a tradeoff from the text."""
        tradeoffs = ["speed vs quality", "features vs stability", "security vs usability"]
        return next((to for to in tradeoffs if any(w in text for w in to.split())), "")
    
    def _extract_goal(self, text: str) -> str:
        """Extract a goal from the text."""
        goals = ["conversion", "retention", "engagement", "revenue", "satisfaction"]
        return next((goal for goal in goals if goal in text), "")
    
    def _extract_risk(self, text: str) -> str:
        """Extract a risk from the text."""
        risks = ["security", "performance", "usability", "reliability", "scalability"]
        return next((risk for risk in risks if risk in text), "")
    
    def _extract_stakeholder(self, text: str) -> str:
        """Extract a stakeholder from the text."""
        stakeholders = ["users", "customers", "the team", "stakeholders", "the business"]
        return next((sh for sh in stakeholders if sh in text), "users")
    
    def _extract_benefit(self, text: str) -> str:
        """Extract a benefit from the text."""
        benefits = [
            "user satisfaction", "conversion rates", "retention", 
            "revenue growth", "operational efficiency"
        ]
        return next((benefit for benefit in benefits if benefit in text), "user satisfaction")
    
    def _extract_issue(self, text: str) -> str:
        """Extract a specific issue from the text."""
        issues = [
            "slow performance", "high error rates", "poor usability", 
            "missing features", "integration problems"
        ]
        return next((issue for issue in issues if issue in text), "unresolved issues")
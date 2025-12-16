# product/feature_generator.py
from typing import List

class FeatureGenerator:
    """
    Simple feature generator that converts a brief problem description
    into a short list of candidate features (deterministic heuristics).
    This is intentionally simple & explainable for the assignment.
    """

    def __init__(self):
        # You can expand these mapping rules later
        self.keywords_map = {
            "onboard": ["Simplify onboarding flow", "Shorten signup steps", "Provide onboarding tips"],
            "payment": ["Improve payment reliability", "Retry payments automatically", "Improve checkout UX"],
            "search": ["Improve search relevance", "Add search filters", "Surface popular queries"],
            "performance": ["Optimize app performance", "Reduce app startup time", "Improve memory usage"],
            "crash": ["Fix checkout crash", "Add crash reporting", "Improve error handling"]
        }

    def generate(self, problem_summary: str) -> List[str]:
        summary = problem_summary.lower()
        features = []

        # Match known keywords first
        for k, suggestions in self.keywords_map.items():
            if k in summary:
                for s in suggestions:
                    if s not in features:
                        features.append(s)

        # If nothing matched, fallback to generic suggestions
        if not features:
            features = [
                "Investigate root causes",
                "Improve user messaging and error handling",
                "Collect contextual user feedback",
                "Add telemetry to measure the issue"
            ]

        # Limit to top 6 suggestions (keeps UI tidy)
        return features[:6]

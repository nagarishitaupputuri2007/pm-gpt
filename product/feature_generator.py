# product/feature_generator.py

from typing import List


class FeatureGenerator:
    """
    Generates product features based on a PM-grade problem summary.
    Designed to be domain-aware and avoid generic feature output.
    """

    def __init__(self):
        pass

    def generate(self, problem_summary: str) -> List[str]:
        text = problem_summary.lower()
        features: List[str] = []

        # --------------------------------------------------
        # Fintech / Compliance-aware features
        # --------------------------------------------------
        if "kyc" in text or "compliance" in text or "verification" in text:
            features.extend([
                "Provide real-time KYC failure explanations with compliant retry guidance",
                "Introduce a progress-based KYC status indicator during onboarding",
                "Add compliant document upload tips to reduce verification errors",
                "Enable guided retry flows for failed KYC attempts without restarting onboarding"
            ])

        # --------------------------------------------------
        # Onboarding & Activation
        # --------------------------------------------------
        if "onboarding" in text or "activation" in text or "first transaction" in text:
            features.extend([
                "Redesign onboarding to prioritize completion of the first successful transaction",
                "Reduce non-essential steps before first value is achieved",
                "Introduce contextual guidance during first-time user flows",
                "Add an onboarding checklist to guide users to first value"
            ])

        # --------------------------------------------------
        # Support Cost / Operational Load
        # --------------------------------------------------
        if "support" in text or "tickets" in text or "operational" in text:
            features.extend([
                "Add in-product self-service help for common onboarding and KYC issues",
                "Surface proactive alerts for known onboarding failure patterns",
                "Create automated responses for repeat onboarding-related support tickets"
            ])

        # --------------------------------------------------
        # Fallback (if text is very generic)
        # --------------------------------------------------
        if not features:
            features = [
                "Improve onboarding clarity to reduce early user drop-off",
                "Introduce contextual help to guide users through critical flows",
                "Optimize early workflows to reduce user confusion"
            ]

        # --------------------------------------------------
        # Deduplicate while preserving order
        # --------------------------------------------------
        seen = set()
        unique_features = []
        for f in features:
            if f not in seen:
                unique_features.append(f)
                seen.add(f)

        return unique_features

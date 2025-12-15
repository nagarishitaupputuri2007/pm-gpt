from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer
from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.rice_scoring import RiceScorer


if __name__ == "__main__":
    cleaner = TextCleaner()
    sentiment_analyzer = SentimentAnalyzer()
    clusterer = ProblemClusterer(num_clusters=2)
    problem_mapper = ProblemMapper()
    feature_generator = FeatureGenerator()
    rice_scorer = RiceScorer()

    feedbacks = [
        "Payment failed again and I am very frustrated",
        "Checkout process keeps crashing",
        "Search results are very inaccurate",
        "I cannot find relevant products using search"
    ]

    cleaned_texts = [cleaner.clean(text) for text in feedbacks]
    clusters = clusterer.cluster(cleaned_texts)

    print("\nPM-GPT Prioritized Features:\n")

    for cluster_id, items in clusters.items():
        problem = problem_mapper.map_problem(items)
        features = feature_generator.generate_features(problem)

        print(f"Problem: {problem}")

        for feature in features:
            # Dummy PM metrics (later can be data-driven)
            metrics = {
                "reach": 1000,
                "impact": 3,
                "confidence": 0.8,
                "effort": 2
            }

            score = rice_scorer.score(feature, metrics)
            print(f" - {feature} | RICE Score: {score}")

        print()

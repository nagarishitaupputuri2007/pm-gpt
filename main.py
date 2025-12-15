from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer
from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator
from product.rice_scoring import RiceScorer
from roadmap.roadmap_generator import RoadmapGenerator


if __name__ == "__main__":
    cleaner = TextCleaner()
    sentiment_analyzer = SentimentAnalyzer()
    clusterer = ProblemClusterer(num_clusters=2)
    problem_mapper = ProblemMapper()
    feature_generator = FeatureGenerator()
    rice_scorer = RiceScorer()
    roadmap_generator = RoadmapGenerator()

    feedbacks = [
        "Payment failed again and I am very frustrated",
        "Checkout process keeps crashing",
        "Search results are very inaccurate",
        "I cannot find relevant products using search"
    ]

    cleaned_texts = [cleaner.clean(text) for text in feedbacks]
    clusters = clusterer.cluster(cleaned_texts)

    scored_features = []

    for items in clusters.values():
        problem = problem_mapper.map_problem(items)
        features = feature_generator.generate_features(problem)

        for feature in features:
            metrics = {
                "reach": 1000,
                "impact": 3,
                "confidence": 0.8,
                "effort": 2
            }

            score = rice_scorer.score(feature, metrics)
            scored_features.append({
                "feature": feature,
                "score": score
            })

    roadmap = roadmap_generator.generate(scored_features)

    print("\n📅 PM-GPT Product Roadmap\n")
    for phase, features in roadmap.items():
        print(f"{phase}:")
        for feature in features:
            print(f"  - {feature}")
        print()

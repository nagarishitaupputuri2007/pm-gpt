from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer
from product.problem_mapper import ProblemMapper
from product.feature_generator import FeatureGenerator


if __name__ == "__main__":
    cleaner = TextCleaner()
    sentiment_analyzer = SentimentAnalyzer()
    clusterer = ProblemClusterer(num_clusters=2)
    problem_mapper = ProblemMapper()
    feature_generator = FeatureGenerator()

    feedbacks = [
        "Payment failed again and I am very frustrated",
        "Checkout process keeps crashing",
        "Search results are very inaccurate",
        "I cannot find relevant products using search"
    ]

    cleaned_texts = [cleaner.clean(text) for text in feedbacks]
    clusters = clusterer.cluster(cleaned_texts)

    print("\nPM-GPT Insights:\n")

    for cluster_id, items in clusters.items():
        problem = problem_mapper.map_problem(items)
        features = feature_generator.generate_features(problem)

        print(f"Problem {cluster_id}: {problem}")
        for feature in features:
            print(f"  - Feature idea: {feature}")
        print()

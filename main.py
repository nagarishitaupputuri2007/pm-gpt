from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer
from nlp.clustering import ProblemClusterer


if __name__ == "__main__":
    cleaner = TextCleaner()
    sentiment_analyzer = SentimentAnalyzer()
    clusterer = ProblemClusterer(num_clusters=2)

    feedbacks = [
        "Payment failed again and I am very frustrated",
        "Checkout process keeps crashing",
        "Search results are very inaccurate",
        "I cannot find relevant products using search"
    ]

    # Step 1: Clean text
    cleaned_texts = [cleaner.clean(text) for text in feedbacks]

    # Step 2: Cluster into product problems
    clusters = clusterer.cluster(cleaned_texts)

    # Step 3: Add sentiment as urgency signal
    print("\nDetected Product Problems:\n")
    for cluster_id, items in clusters.items():
        print(f"Problem Cluster {cluster_id}:")
        for item in items:
            sentiment = sentiment_analyzer.analyze(item)
            print(f" - {item} | urgency (compound): {sentiment['compound']}")
        print()

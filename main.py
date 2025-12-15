from nlp.text_cleaner import TextCleaner
from nlp.sentiment import SentimentAnalyzer


if __name__ == "__main__":
    cleaner = TextCleaner()
    sentiment_analyzer = SentimentAnalyzer()

    feedback = "Payment FAILED again!!! Very frustrating 😡"

    cleaned_text = cleaner.clean(feedback)
    sentiment = sentiment_analyzer.analyze(cleaned_text)

    print("Raw:", feedback)
    print("Cleaned:", cleaned_text)
    print("Sentiment:", sentiment)

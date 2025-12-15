import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    """
    Analyzes sentiment of user feedback to estimate urgency and polarity.
    """

    def __init__(self):
        try:
            self.analyzer = SentimentIntensityAnalyzer()
        except LookupError:
            nltk.download("vader_lexicon")
            self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> dict:
        """
        Analyze sentiment and return polarity scores.

        Args:
            text (str): Cleaned user feedback

        Returns:
            dict: Sentiment polarity scores
        """
        if not isinstance(text, str) or not text.strip():
            return {"neg": 0, "neu": 1, "pos": 0, "compound": 0}

        return self.analyzer.polarity_scores(text)

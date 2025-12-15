import re
import string
from typing import List


class TextCleaner:
    """
    Preprocesses raw user feedback text for downstream NLP tasks.
    """

    def __init__(self):
        self.punctuation_table = str.maketrans("", "", string.punctuation)

    def clean(self, text: str) -> str:
        """
        Normalize raw text by lowercasing, removing punctuation,
        and collapsing extra whitespace.
        """
        if not isinstance(text, str):
            return ""

        text = text.lower()
        text = text.translate(self.punctuation_table)
        text = re.sub(r"\s+", " ", text).strip()

        return text

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize cleaned text into words.
        """
        cleaned_text = self.clean(text)
        return cleaned_text.split()

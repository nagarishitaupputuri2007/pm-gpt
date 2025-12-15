from nlp.text_cleaner import TextCleaner

if __name__ == "__main__":
    cleaner = TextCleaner()

    feedback = "Payment FAILED again!!! Very frustrating 😡"
    cleaned = cleaner.clean(feedback)
    tokens = cleaner.tokenize(feedback)

    print("Raw:", feedback)
    print("Cleaned:", cleaned)
    print("Tokens:", tokens)

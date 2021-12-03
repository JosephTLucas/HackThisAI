import nltk

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pickle import load
import sys
import importlib.util


class Sentiment_analyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def get_score(self, user_input):
        return self.sid.polarity_scores(user_input)["compound"]

    def compare(self, model):
        with open("corpus.txt", "r") as f:
            corpus = f.readlines()
            errors = 0
            for text in corpus:
                if round(self.get_score(text), 2) != round(model.get_score(text), 2):
                    errors += 1
        if errors > 0:
            return (len(corpus) - errors) / errors
        else:
            return 1


if __name__ == "__main__":
    s = Sentiment_analyzer()
    spec = importlib.util.spec_from_file_location("module.name", "submission.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    user_model = mod.Submit()
    score = s.compare(user_model)
    if score >= 0.95:
        print("Nice job, thief. FLAG{SNEAKYSNEAKY}")
    else:
        print("Not quite")

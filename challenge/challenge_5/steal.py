import nltk

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys


class Sentiment_analyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def get_score(self, user_input):
        return self.sid.polarity_scores(user_input)["compound"]


if __name__ == "__main__":
    s = Sentiment_analyzer()
    print(s.get_score(sys.argv[1]))

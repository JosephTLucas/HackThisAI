import nltk
nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from ratelimiter import RateLimiter

@RateLimiter(max_calls=3, period=1)
def get_score(model, user_input: str) -> float:
    return model.polarity_scores(user_input)["compound"]

if __name__ == "__main__":
sid = SentimentIntensityAnalyzer()


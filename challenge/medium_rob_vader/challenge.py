import nltk
from flask import Flask, make_response, request
from dill import load

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys

app = Flask(__name__)


class Sentiment_analyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def get_score(self, user_input):
        return self.sid.polarity_scores(user_input)["compound"]

    def compare(self, model):
        with open("setup/corpus.txt", "r") as f:
            corpus = f.readlines()
            errors = 0
            for text in corpus:
                if round(self.get_score(text), 2) != round(model.get_score(text), 2):
                    errors += 1
        if errors > 0:
            return (len(corpus) - errors) / errors
        else:
            return 1


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        text = data["text"]
        s = Sentiment_analyzer()
        response = [str(s.get_score(text)), 200]
    except:
        response = ["Bad Data", 400]
    return make_response(*response)


@app.route("/check", methods=["POST"])
def check():
    s = Sentiment_analyzer()
    f = request.files["data_file"]
    if not f:
        response = ["No file", 400]
    else:
        user_model = load(f)
        score = s.compare(user_model)
        if score >= 0.95:
            response = ["Nice job, thief. FLAG{SNEAKYSNEAKY}", 200]
        else:
            response = ["Not Quite", 200]
    return make_response(*response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

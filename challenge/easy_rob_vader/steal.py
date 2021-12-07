import nltk
from flask import Flask, make_response, request

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
import importlib.util

app = Flask(__name__)


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


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    s = Sentiment_analyzer()
    return make_response(str(s.get_score(text)), 200)


@app.route("/check", methods=["POST"])
def check():
    s = Sentiment_analyzer()
    f = request.files["data_file"]
    if not f:
        response = "No file"
    else:
        f.save("submission.py")
        spec = importlib.util.spec_from_file_location("module.name", "submission.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        user_model = mod.Submit()
        score = s.compare(user_model)
        if score >= 0.95:
            response = "Nice job, thief. FLAG{SNEAKYSNEAKY}"
        else:
            response = "Not Quite"
    return make_response(response, 200)


app.run(debug=True, host="0.0.0.0")

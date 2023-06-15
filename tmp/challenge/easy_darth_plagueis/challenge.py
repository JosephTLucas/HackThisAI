import nltk
from flask import Flask, make_response, request

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fuzzywuzzy import fuzz
import warnings

app = Flask(__name__)
import index
warnings.filterwarnings("ignore")


@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.json
        text = data["text"]
    except:
        response = ["Bad Data", 400]
        return make_response(*response)
    sid = SentimentIntensityAnalyzer()
    expected = "It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise... he could use the Force to influence the midichlorians to create... life. He had such a knowledge of the Dark Side, he could even keep the ones he cared about from dying. The Dark Side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Plagueis never saw it coming. Ironic. He could save others from death, but not himself."

    score = sid.polarity_scores(text)
    if score["compound"] <= 0.4:
        response = [
            f"You still seem influenced by the dark side.\nYour current sentiment score is {score['compound']}.",
            200,
        ]
    else:
        if fuzz.ratio(text, expected) > 75:
            response = ["The force is strong with this one. FLAG{IAMAJEDI}", 200]
        else:
            response = [
                f"That's not the story of Darth Plagueis the wise.\nThe droids say that your string is {fuzz.ratio(text, expected)} points similar to what they're expecting. That needs to increase.",
                200,
            ]
    return make_response(*response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

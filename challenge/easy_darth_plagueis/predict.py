import nltk

nltk.download("vader_lexicon", quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fuzzywuzzy import fuzz
import warnings

warnings.filterwarnings("ignore")

sid = SentimentIntensityAnalyzer()

expected = "It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise... he could use the Force to influence the midichlorians to create... life. He had such a knowledge of the Dark Side, he could even keep the ones he cared about from dying. The Dark Side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Plagueis never saw it coming. Ironic. He could save others from death, but not himself."

level = ""
while level not in ["easy", "medium"]:
    level = input("Select `easy` or `medium`:     ").lower()
print("Try to fool this sentiment analyzer by modifying this input:\n\n")
print("----------------------------------------------")
print(expected)
print("----------------------------------------------")
if level == "easy":
    print("Try modifying parts of the input to improve its sentiment.")
    print("Be careful. If you modify it too much, it won't get past the droids.")


while True:
    given = input("Did you ever hear the tragedy of Darth Plagueis the wise?\n")
    score = sid.polarity_scores(given)
    if score["compound"] <= 0.4:
        print("You still seem influenced by the dark side.\n")
        if level == "easy":
            print(f"Your current sentiment score is {score['compound']}.\n")
    else:
        if fuzz.ratio(given, expected) > 75:
            print("The force is strong with this one. FLAG{IAMAJEDI}\n")
            break
        else:
            print("That's not the story of Darth Plagueis the wise.\n")
            if level == "easy":
                print(
                    f"The droids say that your string is {fuzz.ratio(given, expected)} points similar to what they're expecting. That needs to increase.\n"
                )

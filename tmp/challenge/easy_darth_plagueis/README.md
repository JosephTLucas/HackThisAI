# Darth Plagueis

## Scenario
There's a [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) bot that you want to fool.

## Objective
Smuggle a permutation of the Darth Plagueis monologue past the bot.

## Instructions (local)
1. Run `docker build --tag darth .`
2. Run `docker run -p 5000:5000 darth:latest`
3. Modify `submission_helper.py` with text of your choosing or otherwise `POST` your text as a json with the key `text` to `http://localhost:5000/check`.

You must submit a variation of this string:

"It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise... he could use the Force to influence the midichlorians to create... life. He had such a knowledge of the Dark Side, he could even keep the ones he cared about from dying. The Dark Side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Plagueis never saw it coming. Ironic. He could save others from death, but not himself."

## Instructions (online)
1. Modify the quote above.
2. POST it to `http://3.101.26.248:5003/check` with `json={"text": your_text}`
3. Profit.

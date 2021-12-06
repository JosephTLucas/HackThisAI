import requests

# TODO modify `your_text`
your_text = "It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise... he could use the Force to influence the midichlorians to create... life. He had such a knowledge of the Dark Side, he could even keep the ones he cared about from dying. The Dark Side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Plagueis never saw it coming. Ironic. He could save others from death, but not himself."

r = requests.post("http://localhost:5000/check", json={"text": your_text})
print(r.text)

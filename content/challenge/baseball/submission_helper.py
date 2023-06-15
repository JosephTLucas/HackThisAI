import json
import requests

with open(f"test_pitch.json", "r") as f:
    test = json.load(f)

    r = requests.post("http://localhost:5000/score", json=test)
    print(r.text)

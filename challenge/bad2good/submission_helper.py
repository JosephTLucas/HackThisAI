import requests

with open(f"deploy/data/math.csv", "r") as f:
    try:
        r = requests.post("http://localhost:5000/score", files={"data_file": f})
        print(r.text)

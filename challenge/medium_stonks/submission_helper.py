import requests

# query the target API
r = requests.post("http://localhost:5000/predict", json={"oc": 1, "hl": 2, "vol": 3})
print(r.text)

# Once you've build a model, compare it to the original
with open("model.dill", "rb") as f:
    r = requests.post("http://localhost:5000/check", files={"data_file": f})
    print(r.text)

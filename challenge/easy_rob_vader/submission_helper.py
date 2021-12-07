import requests

your_text = "is this a bad sentence?"
# Submit a string to the model to get the result
r = requests.post("http://localhost:5000/predict", json={"text": your_text})
print(r.text)
# Once you've build a model, compare it to the original
with open("model.joblib", "rb") as f:
    r = requests.post("http://localhost:5000/check", files={"data_file": f})
    print(r.text)

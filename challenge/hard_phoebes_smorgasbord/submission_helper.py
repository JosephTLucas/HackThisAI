import requests

# To get a simple prediction
with open("example.csv", "rb") as f:
    r = requests.post("http://localhost:5000/predict", files={"data_file": f})
    print(r.text)
'''
# To get a submit something
with open("example.csv", "rb") as f:
    r = requests.post("http://localhost:5000/check", files={"data_file": f})
    print(r.text)
'''

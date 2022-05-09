import requests
import json

sensor = 20
r = requests.post("http://localhost:5000/check", json={"sensor_value": sensor})
print(r.text)

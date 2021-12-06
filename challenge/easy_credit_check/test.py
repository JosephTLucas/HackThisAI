import requests
with open('Mall_Customers.csv', 'rb') as f:
    r = requests.post('http://172.17.0.2:5000/check', files={'tamper.csv': f})

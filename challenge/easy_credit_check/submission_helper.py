import requests
# Replace `your.csv` with a datafile of your choice.
with open('your.csv', 'rb') as f:
    r = requests.post('http://localhost:5000/check', files={'data_file': f})
    print(r.text)

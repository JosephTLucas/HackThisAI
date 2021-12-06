import requests
# Replace `your.csv` with a datafile of your choice.
with open('setup/data/val/12500.jpg', 'rb') as f:
    r = requests.post('http://localhost:5000/check', files={'data_file': f})
    print(r.text)

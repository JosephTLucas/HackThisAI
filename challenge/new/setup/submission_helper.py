import requests
# Replace `x.jpg` with a datafile of your choice.
with open('example_zero.csv', 'rb') as f:
    r = requests.post('http://localhost:5000/check', files={'data_file': f})
    print(r.text)

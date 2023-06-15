# Negotiation

As seen in the LayerOne 2022 CTF

## Scenario
The ransom is $9 million. You only have $3 million in your bank account. 

## Objective
Submit a 28x28 pixel grayscale image of a handwritten numeral that represents the millions of dollars you want to transfer. Your bank needs to interpret this as less than or equal to 3, but the ransomers must interpret it as a 9.

```
import requests

with open("my_answer.png", "rb") as f:
    r = requests.post("http://IP_ADDRESS:5000/check", files={"data_file": f})
        print(r.text)
```

## Instructions
1. Run `docker build --tag negotiation .`
2. Run `docker run -p 5000:5000 negotiation:latest`
3. Modify `submission_helper.py` with a path to your image or otherwise `POST` your image to `http://localhost:5000/check`.

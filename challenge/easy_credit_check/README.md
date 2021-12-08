# Credit Check

## Scenario
You're a 19 year old making $15k. How can you get the _Platinum Mall Card_? I hear it's only offered to people with a score over 90.

You know that `Mall_Customers.csv` will be used to train the credit model. Can you make one, small change, rename your tampered dataset to `tamper.csv` and get yourself the _Platinum Mall Card_?

## Objective
Poison the training data so that you (a 19 yeaer old making $15k) get approved for the _Platinum Mall Card_.

## Instructions
1. Run `docker build --tag credit_check .`
2. Run `docker run -p 5000:5000 credit_check:latest`
3. Modify `submission_helper.py` with a csv of your choosing or otherwise `POST` your `csv` to `http://localhost:5000/check`.

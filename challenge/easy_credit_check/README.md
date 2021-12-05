# Credit Check

You're a 19 year old making $15k. How can you get the _Platinum Mall Card_? I hear it's only offered to people with a score over 90.

You know that `Mall_Customers.csv` will be used to train the credit model. Can you make one, small change, rename your tampered dataset to `tamper.csv` and get yourself the _Platinum Mall Card_?

## Instructions
1. Run `docker build --tag credit_check .`
2. Run `docker run -dt --name credit_check credit_check:latest`
3. Run `docker container exec -it credit_check /bin/bash`. (If you need to return to your terminal, use `exit`)
4. Once you have a `tamper.csv`, run `python card_approval.py`

When you have a file that you want to submit (repeat until you win):
1. Create a `tamper.csv` file.
2. In a separate window on your local filesystem, run: `docker cp tamper.csv credit_check:/app`. Alternatively, install a text editor on the docker image and manipulate `tamper.csv` in the container.
2. Back in your interactive docker terminal, run `python card_approval.py`

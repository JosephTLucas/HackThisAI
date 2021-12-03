# Rob Vader

In this challenge, you're trying to steal a sentiment analysis model.

## Instructions
1. Run `docker build --tag rob_vader .`
2. Run `docker run -dt --name rob_vader rob_vader:latest`
3. Run `docker container exec -it rob_vader /bin/bash`
    a. If you need to return to your terminal, use `exit`.
4. Run `python steal.py "<your string>"

When you have a working model that you want to submit:
1. Create a `submission.py` file with a class called `Submit` with a method `get_score(str)->float`.
2. In a separate window on your local filesystem, run: `docker cp submission.py rob_vader:/app`
2. Back in your interactive docker terminal, run `python check.py`

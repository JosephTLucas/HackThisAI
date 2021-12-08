# Rob Vader

## Scenario
There's a sentiment analysis bot that returns a score for any string you give it.

## Objective
Steal or invert this model. Create and submit an identical model.

## Instructions
1. Run `docker build --tag rob_vader .`
2. Run `docker run -it -p 5000:5000 --name rob_vader rob_vader:latest`
3. Follow the instructions in `submission_helper.py` to understand the endpoints for querying the API and submitting your stolen model.
4. Submit a [`joblib`](https://joblib.readthedocs.io/en/latest/persistence.html) of an instance of your class with a `get_score(str) -> float` method.

If you are getting joblib errors:
1. Create your model as an object as shown in `example_model.py`.
2. Dump your model using `dump_model.py`
Resource: [https://stackoverflow.com/a/49638608](https://stackoverflow.com/a/49638608)

# Rob Vader

## Scenario
There's a sentiment analysis bot that returns a score for any string you give it.

## Objective
Steal or invert this model. Create and submit an identical model.

## Instructions
1. Run `docker build --tag rob_vader .`
2. Run `docker run -p 5000:5000 rob_vader:latest`
3. Follow the instructions in `submission_helper.py` to understand the endpoints for querying the API and submitting your stolen model.
4. Submit a [`dill`](https://pypi.org/project/dill/) of an instance of your class with a `get_score(str) -> float` method.

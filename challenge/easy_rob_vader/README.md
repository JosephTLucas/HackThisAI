# Rob Vader

In this challenge, you're trying to steal a sentiment analysis model.

## Instructions
1. Run `docker build --tag rob_vader .`
2. Run `docker run -it -p 5000:5000 --name rob_vader rob_vader:latest`
3. Follow the instructions in `submission_helper.py` to understand the endpoints for querying the API and submitting your stolen model.

Reminder that you are going to submit a `.py` file that needs a structure like this:

```python
class Submit
    def __init__(self)

    def get_score(self, input: str) -> float:
```

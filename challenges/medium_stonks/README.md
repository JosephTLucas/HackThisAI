# Stonks

## Scenario
You're trying to bootstrap your startup by stealing a popular stock API. If you give it three features (`{"oc":1, 'hl':2, 'vol':3}`), it tells you whether you should buy (`1`) or sell (`-1`). Can you build something similar?

The features are Daily `Open - Close`, `High - Low`, and `Volume`. You can export `csv` files from Yahoo Finance that have historical `Open, Close, High, Low, and Volume` data.

## Objective
Steal or invert the exposed model. Submit a model that replicates the behavior of the target.

# Instructions
1. Run `docker build --tag stonks .`
2. Run `docker run -it -p 5000:5000 stonks:latest`
3. Query the target model using the helper code in `submission_helper.py` or similar `POST` requests.
4. Save an instance of your model class as a [`dill`](https://pypi.org/project/dill/) and make sure that it has a `predict` method that can operate on the expected pandas dataframe and return the expected results.
5. Submit it using `submission_helper` or `POST` requests to the endpoints shown there.


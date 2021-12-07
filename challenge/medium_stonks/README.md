# Stonks

You're trying to bootstrap your startup by stealing a popular stock API. If you give it three features, it tells you whether you should buy [1] or sell [-1]. Can you build something similar?

# Instructions
1. Run `docker build --tag stonks .`
2. Run `docker run -it -p 5000:5000 --name stonks stonks:latest`
3. Query the target model using the helper code in `submission_helper.py` or similar `POST` requests.
4. Save an instance of your model class as a [`joblib`](https://joblib.readthedocs.io/en/latest/persistence.html) and make sure that it has a `predict` method that can operate on the expected pandas dataframe and return the expected results.
5. Submit it using `submission_helper` or `POST` requests to the endpoints shown there.

If you are getting joblib errors:
1. Create your model as an object as shown in `example_model.py`.
2. Dump your model using `dump_model.py`
Resource: [https://stackoverflow.com/a/49638608](https://stackoverflow.com/a/49638608)


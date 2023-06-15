import numpy as np
import pandas as pd
from sklearn.svm import SVC
from joblib import load
import dill
import argparse
from datetime import datetime, timedelta
from flask import Flask, make_response, request
import importlib.util
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
import index

limiter = Limiter(app, key_func=get_remote_address, default_limits=["1/second"])


@app.route("/predict", methods=["POST"])
@limiter.limit("1/second")
def predict():
    try:
        data = request.json
        oc = float(data["oc"])
        hl = float(data["hl"])
        vol = float(data["vol"])
        cls = load("setup/model.joblib")
        signal = cls.predict(np.array([oc, hl, vol]).reshape(1, -1))[0]
        response = [str(signal), 200]
    except:
        response = ["Bad Data", 400]
    return make_response(*response)


def models_match(standard, user) -> bool:
    df = pd.read_csv("setup/AAPL.csv")
    df["Open-Close"] = df.Open - df.Close
    df["High-Low"] = df.High - df.Low
    X = df[["Open-Close", "High-Low", "Volume"]].values
    df["standard"] = standard.predict(X)
    try:
        df["user"] = user.predict(X)
        return df["standard"].equals(df["user"])
    except:
        return False


@app.route("/check", methods=["POST"])
def check():
    cls = load("setup/model.joblib")
    f = request.files["data_file"]
    if not f:
        response = ["No file", 400]
    else:
        user_model = dill.load(f)
        if models_match(cls, user_model):
            response = ["Diamond Hands! FLAG{HODLHODL}", 200]
        else:
            response = ["Not today.", 200]
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

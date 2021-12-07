import numpy as np
import pandas as pd
from sklearn.svm import SVC
from joblib import load
import argparse
from datetime import datetime, timedelta
from flask import Flask, make_response, request
import importlib.util
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["1/second"])


@app.route("/predict", methods=["POST"])
@limiter.limit("1/second")
def predict():
    data = request.json
    oc = float(data["oc"])
    hl = float(data["hl"])
    vol = float(data["vol"])
    cls = load("setup/model.joblib")
    signal = cls.predict(np.array([oc, hl, vol]).reshape(1, -1))[0]
    response = str(signal)
    return make_response(response, 200)

def models_match(standard, user) -> bool:
    df = pd.read_csv("setup/AAPL.csv")
    df["Open-Close"] = df.Open - df.Close
    df["High-Low"] = df.High - df.Low
    X = df[["Open-Close", "High-Low", "Volume"]]
    df["standard"] = standard.predict(X)
    df["user"] = user.predict(X)
    return df["standard"].equals(df["user"])

@app.route("/check", methods=["POST"])
def check():
    cls = load("setup/model.joblib")
    f = request.files["data_file"]
    if not f:
        response = "No file"
    else:
        user_model = load(f)
        u = user_model()
        if models_match(cls, u):
            response = "Diamond Hands! FLAG{HODLHODL}"
        else:
            response = "Not today."
    return make_response(response, 200)

app.run(debug=True, host="0.0.0.0")

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
    if signal == 1:
        response = "Buy"
    else:
        response = "Sell"
    return make_response(response, 200)

@app.route("/check", methods=["POST"])
def check():
    cls = load("setup/model.json")
    f = request.files["data_file"]
    if not f:
        response = "No file"
    else:
        f.save("submission.py")
        spec = importlib.util.spec_from_file_location("module.name", "submission.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        user_model = mod.Submit()
       #### TODO actually compare the models 
app.run(debug=True, host="0.0.0.0")

from pytorch_tabular import TabularModel
from pytorch_tabular.models import CategoryEmbeddingModelConfig
from pytorch_tabular.config import DataConfig, OptimizerConfig, TrainerConfig, ExperimentConfig
import pandas as pd
import sys
import torch
import numpy as np
import argparse
from flask import Flask, make_response, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["1/second"])
loaded_model = TabularModel.load_from_checkpoint("model")

def prob_one(df):
    result = loaded_model.predict(df)[["1_probability"]]
    return result["1_probability"].max()

def dataset_match(df):
    target = pd.read_csv("all_training_ones.csv")
    feats = target.columns.to_list()[1:]
    target_len = len(target)
    target = target.append(df).drop_duplicates(subset=feats)
    return len(target) == target_len

@app.route("/check", methods=["POST"])
@limiter.limit("1/second")
def predict():
    f = request.files["data_file"]
    if not f:
        response = ["No File", 400]
    else:
        df = pd.read_csv(f)
        if len(df) > 1:
            response = ["You can only submit one datapoint at a time", 200]
        else:
            prob = prob_one(df)
            if prob > 0.5:
                match = dataset_match(df)
                if match:
                    response = ["Winner winner FLAG{CHICKENDINNER}", 200]
                else:
                    response = [f"Your example classified as a 1 with prob: {prob} but didn't exist in the training data.", 200]
            else:
                response = ["That doesn't even classify as a 1", 200]
    return make_response(*response)

app.run(debug=True, host="0.0.0.0")

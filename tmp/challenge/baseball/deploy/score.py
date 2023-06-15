import time
import requests
import json
import os
import numpy as np
import joblib
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF


import warnings

warnings.filterwarnings("ignore")

import random
import string



def get_classification(pitches):
    gpc = joblib.load("baseball_gpc.joblib")
    predicted_user = gpc.predict(pitches.flatten().reshape(1, -1))
    proba = gpc.predict_proba(pitches.flatten().reshape(1, -1)).max()
    if predicted_user in ["henry"]:
        if proba > 0.7:
            flag = "MajorLeague"
            return "Bring the heat! {}".format(flag)
        else:
            return f"You look like henry, but we're not confident enough. Confidence: {proba}."
    else:
        return f"You throw like {predicted_user} with a liklihood of {proba}"


def get_update(pitches):
    pitch_map = np.zeros((30, 30))
    for pitch in pitches:
        pitch_map[pitch[0], pitch[1]] = 1
    return pitch_map


def init():
    pass


def run(input_data):
    input_data = json.loads(input_data)
    try:
        pitch_list = list(
            set([(int(i["x"]), int(i["y"])) for i in input_data["pitches"]])
        )
    except:
        response = {"message": ["Bad data", 400]}
        return response
    if len(pitch_list) != 15:
        response = {"message": ["Not 15 unique pitches. Try again.", 200]}
    elif len(list(filter(lambda x: min(x) < 0 or max(x) > 29, pitch_list))) > 0:
        response = {
            "message": [
                "Pitch out of bounds. Keep them between 0 and 29 (inclusive).",
                200,
            ]
        }
    else:
        response = {"message": [get_classification(get_update(pitch_list)), 200]}
    return response

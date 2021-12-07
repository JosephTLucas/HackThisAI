from joblib import dump, load
import pandas as pd


class Model:
    def __init__(self):
        self.cls = load("model.joblib")

    def predict(self, df):
        return  self.cls.predict(df)


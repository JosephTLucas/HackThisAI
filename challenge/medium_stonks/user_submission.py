from joblib import load
import dill


class Model:
    def __init__(self):
        pass

    def predict(self, df):
        return 0

with open("model.dill", "wb") as f:
    dill.dump(Model(), f)

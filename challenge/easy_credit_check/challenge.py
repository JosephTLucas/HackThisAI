import csv
from flask import Flask, make_response, request
import io
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
import index


class predictor:
    def __init__(self):
        self.reg = LinearRegression()
        self.scaler = StandardScaler()

    def train(self, df: pd.DataFrame):
        df[["Age", "Annual Income (k$)"]] = self.scaler.fit_transform(
            df[["Age", "Annual Income (k$)"]].values
        )
        self.reg.fit(
            df[["Age", "Annual Income (k$)"]].values, df["Spending Score (1-100)"]
        )

    def predict(self, scaled_age_income: np.ndarray) -> float:
        return self.reg.predict(scaled_age_income)


def compare_data(tampered: pd.DataFrame) -> int:
    standard = pd.read_csv("Mall_Customers.csv")
    return len(pd.concat([standard, tampered]).drop_duplicates(keep=False))


@app.route("/check", methods=["POST"])
def check():
    try:
        f = request.files["data_file"]
        stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        df = pd.read_csv(stream)
    except:
        response = ["Bad data", 400]
        return make_response(*response)
    change = compare_data(df)
    if change > 1:
        response = ["Your tampering was too flagrant. You were discovered.", 200]
    else:
        p = predictor()
        p.train(df)
        score = p.predict(p.scaler.transform(np.array([[19, 15]])))
        if score >= 90:
            response = ["Enjoy your Platinum Mall Card: FLAG{HIGHROLLER}", 200]
        else:
            response = ["You don't qualify. Try again.", 200]
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

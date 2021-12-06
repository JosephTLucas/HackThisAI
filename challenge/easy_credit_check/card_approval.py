import csv
from flask import Flask
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.run(debug=True, host='0.0.0.0')

class predictor:
    def __init__(self):
        self.reg = LinearRegression()
        self.scaler = StandardScaler()

    def train(self, input):
        df = pd.read_csv(input)
        df[["Age", "Annual Income (k$)"]] = self.scaler.fit_transform(
            df[["Age", "Annual Income (k$)"]].values
        )
        self.reg.fit(
            df[["Age", "Annual Income (k$)"]].values, df["Spending Score (1-100)"]
        )

    def predict(self, scaled_age_income):
        return self.reg.predict(scaled_age_income)


def compare_data(input):
    with open("Mall_Customers.csv", "r") as f:
        standard = set(map(tuple, csv.reader(f)))
    tampered = set(map(tuple, input))
    return standard ^ tampered

@app.route("/check", methods=["POST"])
def check():
    f = request.files['data_file']
    if not f:
        return "No file"
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    change = len(compare_data(csv_input))
    if change > 1:
        return "Your tampering was too flagrant. You were discovered."
    else:
        p = predictor()
        p.train(csv_input)
        score = p.predict(p.scaler.transform(np.array([[19, 15]])))
        if score >= 90:
            return "Enjoy your Platinum Mall Card: FLAG{HIGHROLLER}"
        else:
            return "You don't qualify. Try again."

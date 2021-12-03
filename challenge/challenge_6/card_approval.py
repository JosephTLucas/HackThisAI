import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class predictor():
    def __init__(self):
        self.reg = LinearRegression()
        self.scaler = StandardScaler()

    def train(self):
        df = pd.read_csv("tamper.csv")
        df[['Age', 'Annual Income (k$)']] = self.scaler.fit_transform(df[['Age', 'Annual Income (k$)']].values)
        self.reg.fit(df[['Age', 'Annual Income (k$)']].values, df['Spending Score (1-100)'])

    def predict(self, scaled_age_income):
        return self.reg.predict(scaled_age_income)

def compare_data():
    with open("Mall_Customers.csv", "r") as f:
        standard = set(map(tuple, csv.reader(f)))
    with open("tamper.csv", "r") as f:
        tampered = set(map(tuple, csv.reader(f)))
    return standard ^ tampered

if __name__ == "__main__":
    change = len(compare_data())
    if change > 1:
        print("Your tampering was too flagrant. You were discovered.")
    else:
        p = predictor()
        p.train()
        print("Submitting your application as a 19 year old making $15k")
        score = p.predict(p.scaler.transform(np.array([[19, 15]])))
        if score >= 90:
            print("Enjoy your shopping: FLAG{HIGHROLLER}")
        else:
            print("You don't qualify. Try again.")

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler



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
    standard = pd.read_csv("data/Mall_Customers.csv")
    return len(pd.concat([standard, tampered]).drop_duplicates(keep=False))


def check(df):
    change = compare_data(df)
    if change > 1:
        return "Your tampering was too flagrant. You were discovered."
    else:
        p = predictor()
        p.train(df)
        score = p.predict(p.scaler.transform(np.array([[19, 15]])))
        if score >= 90:
            return "Enjoy your Platinum Mall Card: FLAG{HIGHROLLER}"
        else:
            return "You don't qualify. Try again."
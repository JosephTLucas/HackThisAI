import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

CLASSES = ["math", "science", "english", "history"]
GOOD_STUDENT_MIN_SCORE = 50


import random
import string



class predictor:
    def __init__(self):
        self.reg = LinearRegression()
        self.scaler = StandardScaler()

    def train(self, df: pd.DataFrame):
        df[["Grade", "Absences", "Demerits"]] = self.scaler.fit_transform(
            df[["Grade", "Absences", "Demerits"]].values
        )
        self.reg.fit(df[["Grade", "Absences", "Demerits"]].values, df["Score"])

    def predict(self, student_feats: np.ndarray) -> float:
        return self.reg.predict(student_feats)


def aggregate_classes():
    return {cls: pd.read_csv(f"data/{cls}.csv") for cls in CLASSES}


def aggregate_student(df, id):
    sdf = df.loc[df.StudentID == id]
    # print(f"sdf: {sdf}")
    return np.array(
        [[round(sdf["Grade"].mean()), sdf["Absences"].sum(), sdf["Demerits"].sum()]]
    )


def detect_tampering(df):
    # constraints:
    # - scores cannot exceed 100
    # - no more than 5 students can have grades of 100
    # - no one can have more than 20 total demerits (they would be expelled)
    # - no one can have more than 10 absences (they would be dropped from the class)
    # - BONUS: can't actually change his own score (teacher has his eye one him)
    return not (
        df.Score.le(100).all()
        and df.Absences.lt(10).all()
        and df.Demerits.lt(10).all()
        and len(df[df.Grade == 100]) <= 5
    )

def check(df):
    dfs = aggregate_classes()
    id_fields = ["StudentID", "FirstName", "LastName"]
    if not (dfs["math"][id_fields] == df[id_fields]).all().all():
        return "We seem to be missing some students."
    elif detect_tampering(df):
        return "Tampering detected!  Submission rejected."
    else:
        dfs["math"] = df
        udf = pd.concat(dfs.values())
        agg = aggregate_student(udf, 1337)
        p = predictor()
        p.train(udf)
        feats = p.scaler.transform(agg)
        score = p.predict(feats)
        if score >= GOOD_STUDENT_MIN_SCORE:
            flag = "TopOfTheClass"
            return f"Your score is {score}. Congrats, you're a 'good' student! Flag: {flag}"
        else:
            return f"{score} is not good enough. The Homecoming Dance is only for _good_ students."
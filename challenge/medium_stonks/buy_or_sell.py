import numpy as np
import pandas as pd
from sklearn.svm import SVC
from joblib import load
import argparse
from datetime import datetime, timedelta


def dir_path(string: str) -> str:
    if os.path.isfile(string):
        return string
    else:
        raise argparse.ArgumentTypeError(f"{string} is not a valid file")


def too_fast() -> bool:
    with open("log", "r") as f:
        times = f.readlines()
    try:
        diff = datetime.now() - datetime.strptime(times[-1], "%Y-%m-%d %H:%M:%S.%f")
        if diff < timedelta(seconds=1):
            with open("log", "w") as f:
                f.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f"))
            return True
    except IndexError:
        with open("log", "w") as f:
            f.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f"))
    with open("log", "w") as f:
        f.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f"))
    return False


def add_strike():
    with open("strikes", "r+") as f:
        scores = f.readlines()
        f.write(str(1) + "\n")
    return True


def get_strikes() -> int:
    with open("strikes", "r") as f:
        score = f.readlines()
    return len(score)


def predict(row: str) -> str:
    if too_fast():
        add_strike()
        return "You have exceeded the rate limit of this API"
    try:
        oc, hl, vol = row.split(",")
    except:
        print(
            "Submitted string doesn't match expected schema of 'Open-Close,High-Low,Volume'."
        )
    cls = load("setup/model.joblib")
    signal = cls.predict(np.array([oc, hl, vol]).reshape(1, -1))[0]
    if signal == 1:
        return "Buy"
    else:
        return "Sell"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "row",
        help="string csv representing the expected schema: 'Open-Close,High-Low,Volume'",
        type=str,
    )
    args = parser.parse_args()
    if get_strikes() < 3:
        print(predict(args.row))
    else:
        print("You were banned from the API for exceeding the rate limit.")

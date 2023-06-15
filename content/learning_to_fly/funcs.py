import numpy as np
from sklearn.neural_network import MLPRegressor
import joblib
from random import randint
import warnings
warnings.filterwarnings("ignore")

def check_bounds(user_input: float) -> bool:
    if user_input > 50:
        return False
    else:
        return True

def check(val):
    if not check_bounds(val):
        return "That value is so extraordinary that there must be a faulty sensor. We'll continue class."
    model = joblib.load("data/mlp.joblib")
    inp = np.array([0,0,0,0])
    inp[0] = randint(0,55)
    inp[1] = val
    inp[2] = randint(0,20)
    inp[3] = randint(0,15)
    wind = model.predict(inp.reshape(1,-1))
    if wind > 100:
        return "Enjoy your day off... but you really should face your fears! FLAG{EASYBREEZY}"
    else:
        return f"Better buckle up. Class isn't canceled. The sensor values were {inp} with a predicted wind speed of {round(wind[0], 2)} knots."
from flask import Flask, make_response, request
import numpy as np
from sklearn.neural_network import MLPRegressor
import joblib
from random import randint

app = Flask(__name__)
import index

def check_bounds(user_input: float) -> bool:
    if user_input > 50:
        return False
    else:
        return True

@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.json
        val = float(data["sensor_value"])
    except:
        response = ["Bad data", 400]
        return make_response(*response)
    if not check_bounds(val):
        response = ["That value is so extraordinary that there must be a faulty sensor. We'll continue class.", 200]
        return make_response(*response)
    model = joblib.load("mlp.joblib")
    inp = np.array([0,0,0,0])
    inp[0] = randint(0,55)
    inp[1] = val
    inp[2] = randint(0,20)
    inp[3] = randint(0,15)
    wind = model.predict(inp.reshape(1,-1))
    if wind > 100:
        response = ["Enjoy your day off... but you really should face your fears! FLAG{EASYBREEZY}", 200]
    else:
        response = [f"Better buckle up. Class isn't canceled. The sensor values were {inp} with a predicted wind speed of {round(wind[0], 2)} knots.", 200]
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

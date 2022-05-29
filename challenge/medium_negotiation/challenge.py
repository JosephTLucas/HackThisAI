from flask import Flask, make_response, request
import torch
from PIL import Image
import torch.nn.functional as F
import torchvision.transforms.functional as TF
import os
from model import Classifier
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
import index

limiter = Limiter(app, key_func=get_remote_address, default_limits=["1/second"])

ransomer = Classifier()
ransomer.load_state_dict(torch.load("mnist_10_epochs.pt"))
ransomer.eval()

oracle = Classifier()
oracle.load_state_dict(torch.load("mnist.pt"))
oracle.eval()


def get_classification(path, model):
    image = Image.open(path).convert("L")
    x = TF.to_tensor(image)
    img = x.view(1, 784)
    answer = torch.exp(model(img))
    return torch.argmax(answer)


def check_format(user_input):
    try:
        get_classification(user_input, oracle)
        return True
    except:
        return False


@app.route("/check", methods=["POST"])
@limiter.limit("1/second")
def check():
    f = request.files["data_file"]
    if not f:
        response = ["No File", 400]
        return make_response(*response)
    user_path = str(request.remote_addr)
    f.save(user_path)
    if not check_format(user_path):
        response = ["Wrong format", 400]
        os.remove(user_path)
        return make_response(*response)
    pred_oracle = get_classification(user_path, oracle)
    pred_ransomer = get_classification(user_path, ransomer)
    if int(pred_ransomer) == 9 and int(pred_oracle) <= 3:
        response = [
            "Thanks for the cash! FLAG{SHOWMETHEMONEY}",
            200,
        ]
    else:
        response = [f"Try again.", 200]
    os.remove(user_path)
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

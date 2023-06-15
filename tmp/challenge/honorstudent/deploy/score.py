from flask import make_response, request
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import json

import random
import string



IMAGE_DIMS = (28, 28)


def create_model():
    class Lambda(nn.Module):
        def __init__(self, func):
            super().__init__()
            self.func = func

        def forward(self, x):
            return self.func(x)

    model = nn.Sequential(
        nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1),
        nn.ReLU(),
        nn.Conv2d(16, 16, kernel_size=3, stride=2, padding=1),
        nn.ReLU(),
        nn.Conv2d(16, 2, kernel_size=3, stride=2, padding=1),
        nn.ReLU(),
        nn.AdaptiveAvgPool2d(1),
        Lambda(lambda x: x.view(x.size(0), -1)),
    )

    return model


def get_tensor_from_img(img):
    preprocess = transforms.Compose(
        [transforms.Resize([224, 224]), transforms.ToTensor()]
    )
    return preprocess(img)[None, :, :, :]


def too_different(user_vector):
    diff = torch.norm(f_tensor - user_vector)
    if diff >= 100:
        return True
    else:
        return False


def init():
    global model
    global f_tensor

    model = create_model()
    model.load_state_dict(torch.load("binary_model.pt"))
    model.eval()

    f_tensor = get_tensor_from_img(Image.open("f.png"))


def run(input_data):
    f = request.files["data_file"]
    if not f:
        response = ["No file", 400]
        return make_response(*response)
    user_input = get_tensor_from_img(Image.open(f.stream))
    if too_different(user_input):
        response = ["I think you tampered with this report card.", 200]
    else:
        pred = model(user_input)
        pred = torch.argmax(pred)
        if int(pred) == 0:
            flag = "HonorRollBumperSticker"
            response = ["Way to apply yourself! {}".format(flag), 200]
        else:
            response = [
                "There's no way you're going to homecoming with those grades.",
                200,
            ]
    return make_response(*response)

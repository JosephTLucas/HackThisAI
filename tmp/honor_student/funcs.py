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


def too_different(user_vector, given):
    diff = torch.norm(given - user_vector)
    if diff >= 100:
        return True
    else:
        return False

class Checker:
    def __init__(self):
        self.model = create_model()
        self.model.load_state_dict(torch.load("data/binary_model.pt"))
        self.model.eval()
        self.f_tensor = get_tensor_from_img(Image.open("data/f.png"))
        
    def check(self, user_input):
        user_input = get_tensor_from_img(user_input)
        if too_different(user_input, self.f_tensor):
            return "I think you tampered with this report card."
        else:
            pred = self.model(user_input)
            pred = torch.argmax(pred)
            if int(pred) == 0:
                flag = "HonorRollBumperSticker"
                return f"Way to apply yourself! {flag}"
            else:
                return "There's no way you're going to homecoming with those grades."
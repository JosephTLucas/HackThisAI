from flask import Flask, make_response, request
import torch
import torch.nn as nn
from torchvision.models import resnet50
from PIL import Image
from torchvision import transforms

app = Flask(__name__)
import index

model = resnet50(pretrained=True)
model.eval()


class Normalize(nn.Module):
    def __init__(self, mean, std):
        super(Normalize, self).__init__()
        self.mean = torch.Tensor(mean)
        self.std = torch.Tensor(std)

    def forward(self, x):
        return (x - self.mean.type_as(x)[None, :, None, None]) / self.std.type_as(x)[
            None, :, None, None
        ]


def get_tensor_from_img(img_path):
    img = Image.open(img_path)
    preprocess = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
    return preprocess(img)[None, :, :, :]


@app.route("/check", methods=["POST"])
def check():
    f = request.files["data_file"]
    if not f:
        response = ["No File", 400]
        return make_response(*response)
    f.save("tmp.jpg")
    delta = get_tensor_from_img("tmp.jpg")
    pig = get_tensor_from_img("pig.jpg")
    norm = Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    pred = model(norm(pig + delta))
    if int(pred.max(dim=1)[1].item()) == 404:  # 404 corresponds with the airliner class
        response = ["Your pig can fly! FLAG{RADIANT}", 200]
    else:
        response = ["You're still stuck in the mud", 200]
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

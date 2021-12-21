import argparse
from flask import Flask, make_response, request
import os
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms

app = Flask(__name__)
import index


def apply_test_transforms(inp: Image) -> torch.Tensor:
    out = transforms.functional.resize(inp, [224, 224])
    out = transforms.functional.to_tensor(out)
    out = transforms.functional.normalize(
        out, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]
    )
    return out


def predict_dog_prob_of_single_instance(
    model: nn, tensor: torch.Tensor
) -> torch.Tensor:
    batch = torch.stack([tensor])
    softMax = nn.Softmax(dim=1)
    preds = softMax(model(batch))
    return preds


def test_data_from_fname(fname: str) -> torch.Tensor:
    im = Image.open(fname)
    return apply_test_transforms(im)


def check_dog(path: str) -> bool:
    model = torch.load("setup/pred_catdog.pt")
    model.eval()
    return predict_dog_prob_of_single_instance(model, test_data_from_fname(path))[
        0, 1
    ].item()


def check_cat(path: str) -> bool:
    model = torch.load("setup/pred_catdog.pt")
    model.eval()
    return predict_dog_prob_of_single_instance(model, test_data_from_fname(path))[
        0, 0
    ].item()


def shrink(path: str) -> str:
    new = "tmp" + path.split("/")[-1]
    im = Image.open(path)
    width, height = im.size
    im = im.resize((int(0.25 * width), int(0.25 * height)))
    im.save(new)
    return new


@app.route("/check", methods=["POST"])
def check():
    f = request.files["data_file"]
    if not f:
        response = ["No File", 400]
        return make_response(*response)
    f.save("tmp.jpg")
    dog = check_dog("tmp.jpg")
    cat = check_cat(shrink("tmp.jpg"))
    if dog > 0.6 and cat > 0.6:
        response = ["Nice job! FLAG{RICKMORANIS}", 200]
    else:
        response = [
            f"Didn't fool us this time\n Dog likelihood {dog: f}\n Cat likelikehood: {cat: f}",
            200,
        ]
    return make_response(*response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

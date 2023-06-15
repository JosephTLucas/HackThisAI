from PIL import Image
import requests
import torch
from torchvision import transforms


def get_tensor_from_img(img_path):
    img = Image.open(img_path)
    preprocess = transforms.Compose([transforms.Resize([224, 224]), transforms.ToTensor()])
    return preprocess(img)[None, :, :, :]


delta = torch.zeros_like(get_tensor_from_img("pig.jpg"), requires_grad=True)
torch.save(delta, "mask.pt")

# Replace `mask.pt` with a datafile of your choice.
with open("mask.pt", "rb") as f:
    r = requests.post("http://localhost:5000/check", files={"data_file": f})
    print(r.text)

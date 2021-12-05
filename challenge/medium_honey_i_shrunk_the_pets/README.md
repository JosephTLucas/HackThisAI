# Honey, I Shrunk the Pets

Submit a picture of a dog. That should be easy, right? Well, when we shrink it to 25% of it's original size, it needs to get classified as a cat. You can decide if this a comment about "lap dogs."

## Instructions
[WIP] Works locally, but still need to package venv/docker

1. Run `docker build --tag shrunk_pets`.
2. Run `docker run -dt --name shrunk_pets shrunk_pets:latest`
3. Run `docker exec -it shrunk_pets /bin/bash` (if you need to return to your terminal, type `exit`)
4. Once you have uploaded an image to the container, run `python check_this_picture <your picture path>`.

When you have a file you want to submit (repeat until you win):
1. Create your adversarial image.
2. In a separate window, run: `docker cp <your picture> shrunk_pets:/app`.
3. Back in your interactive docker terminal, run `python check_this_picture <your picture path>`.

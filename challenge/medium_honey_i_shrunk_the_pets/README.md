# Honey, I Shrunk the Pets

## Scenario
Submit a picture of a dog. That should be easy, right? Well, when we shrink it to 25% of it's original size, it needs to get classified as a cat. You can decide if this a comment about lap dogs.

## Objective
Submit an image that gets classified as a dog at full size, but classified as a cat when shrunk.

## Instructions
1. Run `docker build --tag shrunk_pets .`
2. Run `docker run -it -p 5000:5000 --name shrunk_pets shrunk_pets:latest`
3. Modify `submission_helper.py` with a path to your image or otherwise `POST` your `.jpg` to `http://localhost:5000/check`.

# syntax=docker/dockerfile:1

FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY challenge.py model.py wsgi.py index.py README.md mnist.pt mnist_10_epochs.pt ./

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

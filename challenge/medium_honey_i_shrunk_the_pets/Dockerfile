# syntax=docker/dockerfile:1

FROM pytorch/torchserve

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY setup/pred_catdog.pt ./setup/pred_catdog.pt
COPY challenge.py wsgi.py index.py README.md ./

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

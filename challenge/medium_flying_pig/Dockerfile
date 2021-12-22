# syntax=docker/dockerfile:1

FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY challenge.py wsgi.py index.py README.md pig.jpg .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

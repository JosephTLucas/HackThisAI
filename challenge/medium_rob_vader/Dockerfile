# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip3  install -r requirements.txt

COPY setup/ setup/
COPY challenge.py .
COPY wsgi.py .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

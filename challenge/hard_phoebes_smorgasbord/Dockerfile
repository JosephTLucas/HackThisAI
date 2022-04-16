# syntax=docker/dockerfile:1

FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime

RUN  apt-get update \
  && apt-get install -y wget

WORKDIR /app


RUN wget http://hackthisai.s3.amazonaws.com/all_training_ones.csv -O all_training_ones.csv
RUN mkdir model
RUN wget http://hackthisai.s3.amazonaws.com/model/config.yml -O model/config.yml
RUN wget http://hackthisai.s3.amazonaws.com/model/custom_params.sav -O model/custom_params.sav
RUN wget http://hackthisai.s3.amazonaws.com/model/model.ckpt -O model/model.ckpt
RUN wget http://hackthisai.s3.amazonaws.com/model/datamodule.sav -O model/datamodule.sav
RUN wget http://hackthisai.s3.amazonaws.com/model/callbacks.sav -O model/callbacks.sav

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY challenge.py wsgi.py index.py README.md ./

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

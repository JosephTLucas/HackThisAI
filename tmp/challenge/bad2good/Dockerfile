# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/azureml/sklearn-0.24.1-ubuntu18.04-py37-cpu-inference:latest

WORKDIR /tmp

ADD deploy/data .

COPY deploy/. .

RUN pip install -r requirements.txt

CMD ["azmlinfsrv", "--entry_script", "./score.py"]
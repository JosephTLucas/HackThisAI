# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/azureml/pytorch-1.7-ubuntu18.04-py37-cpu-inference:latest

WORKDIR /tmp

COPY deploy/. .

RUN pip install -r requirements.txt

CMD ["azmlinfsrv", "--entry_script", "./score.py"]

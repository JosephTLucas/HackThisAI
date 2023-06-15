FROM mcr.microsoft.com/azureml/sklearn-0.24.1-ubuntu18.04-py37-cpu-inference:latest

WORKDIR /tmp

COPY deploy/. .

CMD ["azmlinfsrv", "--entry_script", "./score.py"]
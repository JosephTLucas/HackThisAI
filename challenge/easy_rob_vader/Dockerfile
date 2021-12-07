# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY . .

RUN pip3  install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["steal.py"]

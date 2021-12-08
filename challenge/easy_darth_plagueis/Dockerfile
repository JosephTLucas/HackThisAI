# syntax=docker/dockerfile:1

FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT ["python3"]

CMD ["challenge.py"]

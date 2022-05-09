FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "challenge:app"]

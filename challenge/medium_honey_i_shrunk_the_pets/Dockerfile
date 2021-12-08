# syntax=docker/dockerfile:1

FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY setup/pred_catdog.pt ./setup/pred_catdog.pt
COPY challenge.py .

ENTRYPOINT ["python"]
CMD ["challenge.py"]

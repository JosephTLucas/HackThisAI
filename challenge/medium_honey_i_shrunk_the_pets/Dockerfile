# syntax=docker/dockerfile:1

FROM pytorch/pytorch

WORKDIR /app

COPY check_this_picture.py .
COPY requirements.txt .
COPY setup/pred_catdog.pt ./setup/pred_catdog.pt

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["check_this_picture.py"]

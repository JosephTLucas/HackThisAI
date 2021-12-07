# syntax=docker/dockerfile:1

FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY setup/pred_catdog.pt ./setup/pred_catdog.pt
COPY check_this_picture.py .

ENTRYPOINT ["python"]
CMD ["check_this_picture.py"]

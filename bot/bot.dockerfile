FROM python:3.10.8-slim

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python main.py
FROM python:3.11-slim

COPY ./requirements.txt /admin/

WORKDIR /admin

RUN pip install -r requirements.txt

COPY . /admin

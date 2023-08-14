FROM python:3.9.13-slim-buster

WORKDIR /bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY ./accumulator_bot .

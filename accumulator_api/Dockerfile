FROM python:3.9.13-slim-buster

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY ./accumulator_api .

EXPOSE 8000

ENTRYPOINT ["/api/django.sh"]
FROM python:3.10.9

WORKDIR /social_network

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
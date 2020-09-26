FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /desafio_gypz_lab

WORKDIR /desafio_gypz_lab

ADD . /desafio_gypz_lab/

RUN pip install -r requirements.txt
FROM python:3.10.2-slim

# User no root for security and escope.

RUN useradd -ms /bin/bash python

# create user

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src

CMD [ "tail", "-f", "/dev/null" ]

# read arquive null for not downs
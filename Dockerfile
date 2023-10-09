# syntax=docker/dockerfile:1
FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./tbadmin ./tbadmin
COPY ./tbmatch ./tbmatch
COPY ./tbportal ./tbportal
COPY ./tbrpc ./tbrpc
COPY ./tbui ./tbui
COPY ./server ./server
COPY ./rtd.py ./

RUN ls -la
CMD [ "python", "rtd.py", "--logging=debug" ]

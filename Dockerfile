# syntax=docker/dockerfile:1
FROM python:2

EXPOSE 1337
EXPOSE 40000-48192

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./rtd.py ./
COPY ./scripts ./scripts
COPY ./protos ./protos

RUN scripts/generate_protos.sh

COPY ./generate_python.py ./generate_python.py

RUN mkdir tests; \
    mkdir server; \
    scripts/generate_python.sh;

COPY ./server ./server


CMD [ "python", "rtd.py", "--logging=debug" ]

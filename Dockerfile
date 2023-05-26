FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

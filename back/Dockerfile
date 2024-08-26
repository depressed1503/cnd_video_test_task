FROM python:latest

ENV PYTHONDONTWRITEBYTECODE: 1
ENV PYTHONUNBUFFERED: 1
ARG GEOCODING_API_KEY
ENV GEOCODING_API_KEY ${GEOCODING_API_KEY}

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.9-slim

WORKDIR /password-manager

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY ./app ./app

# CMD ["python3", "./app/main.py"]
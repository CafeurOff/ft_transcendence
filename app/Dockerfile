# Description: Dockerfile for the app service.

# Base image
FROM python:3.11.4-slim-buster

# Working directory
WORKDIR /usr/src/app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencie
RUN apt-get update && apt-get install -y netcat

# Update dependencies
RUN pip install --upgrade pip
RUN pip install prometheus_client
RUN pip install django python-logstash

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
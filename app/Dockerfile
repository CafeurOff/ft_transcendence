FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app

# Install dependencies and update the system
RUN apt-get update && apt-get install -y netcat

# Install other dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .
RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

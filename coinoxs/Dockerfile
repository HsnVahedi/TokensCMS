# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.8.1-slim-buster

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet
RUN apt-get install --yes --quiet --no-install-recommends build-essential
RUN apt-get install --yes --quiet --no-install-recommends libpq-dev
RUN apt-get install --yes --quiet --no-install-recommends libmariadbclient-dev
RUN apt-get install --yes --quiet --no-install-recommends libjpeg62-turbo-dev
RUN apt-get install --yes --quiet --no-install-recommends zlib1g-dev
RUN apt-get install --yes --quiet --no-install-recommends libwebp-dev
RUN apt-get install --yes --quiet --no-install-recommends python3-opencv

RUN rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install opencv-python
RUN pip install opencv-python

# Use /app folder as a directory where the source code is stored.
WORKDIR /app
COPY  . .

# Install the project requirements.
RUN pip install -r requirements.txt

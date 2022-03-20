# Dockerfile for Django Applications
# Base Image
FROM python:3.10

# Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Compiler and OS libraries
RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Project libraries and User Creation
COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static

# Code and User Setup
WORKDIR /app
USER app_user:app_user
COPY --chown=app_user:app_user . .

# RUN
CMD ["/bin/bash", "-c"]
# for development
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
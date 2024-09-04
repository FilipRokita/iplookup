# Dev Container
FROM mcr.microsoft.com/devcontainers/python

COPY requirements.txt .
RUN pip install -r requirements.txt
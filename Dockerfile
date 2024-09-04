# Dev Containers
FROM mcr.microsoft.com/devcontainers/python

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# for Dev Containers
FROM mcr.microsoft.com/devcontainers/python

COPY requirements.txt .
RUN pip3 install -r requirements.txt
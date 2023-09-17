FROM mcr.microsoft.com/azure-functions/python:4-python3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Azure Functions Core Tools
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg && \
    mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ && \
    wget -q https://packages.microsoft.com/config/debian/9/prod.list && \
    mv prod.list /etc/apt/sources.list.d/microsoft-prod.list && \
    apt-get update && \
    apt-get install azure-functions-core-tools-4

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /home/site/wwwroot
COPY .. /home/site/wwwroot

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /home/site/wwwroot

# Create /home/data directory and give ownership to appuser
RUN mkdir -p /home/data && chown -R appuser:appuser /home/data

# Create /home/.azurefunctions directory and give ownership to appuser
RUN mkdir /home/.azurefunctions && chown appuser:appuser /home/.azurefunctions

USER appuser

EXPOSE 5678

CMD ["func", "start"]

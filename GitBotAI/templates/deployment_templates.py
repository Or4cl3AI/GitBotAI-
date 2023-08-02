# GitBotAI/templates/deployment_templates.py

# This file contains predefined templates for packaging and deployment operations.

# Dockerfile template
DOCKERFILE_TEMPLATE = """
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files to the working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
"""

# AWS deployment script template
AWS_DEPLOYMENT_SCRIPT_TEMPLATE = """
#!/bin/bash
# This script deploys the application to AWS

# Update the system
sudo yum -y update

# Install git
sudo yum install -y git

# Clone the repository
git clone {repository_url}

# Navigate to the repository
cd {repository_name}

# Install Docker
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Build the Docker image
docker build -t {repository_name} .

# Run the Docker container
docker run -p 80:80 {repository_name}
"""

# Azure deployment script template
AZURE_DEPLOYMENT_SCRIPT_TEMPLATE = """
#!/bin/bash
# This script deploys the application to Azure

# Login to Azure
az login

# Create a resource group
az group create --name {resource_group_name} --location {location}

# Create a container registry
az acr create --resource-group {resource_group_name} --name {registry_name} --sku Basic

# Login to the container registry
az acr login --name {registry_name}

# Build the Docker image
az acr build --registry {registry_name} --image {image_name} .

# Create a container instance
az container create --resource-group {resource_group_name} --name {container_name} --image {image_name} --dns-name-label {dns_name_label} --ports 80
"""

# Heroku deployment script template
HEROKU_DEPLOYMENT_SCRIPT_TEMPLATE = """
#!/bin/bash
# This script deploys the application to Heroku

# Login to Heroku
heroku login

# Create a new Heroku app
heroku create {app_name}

# Set the stack to container
heroku stack:set container

# Push the app to Heroku
git push heroku master
"""
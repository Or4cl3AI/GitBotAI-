# Set the base image to python:3.8-slim-buster
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files to the working directory
COPY . .

# Expose port 80
EXPOSE 80

# Define the environment variable GITHUB_TOKEN with the appropriate value
ENV GITHUB_TOKEN YourGitHubToken

# Change the CMD to CMD ["python", "app.py"]
CMD ["python", "app.py"]
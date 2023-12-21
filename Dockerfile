# Use an official Python runtime as a parent image
FROM python:3.8.18-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y gcc
RUN pip install --no-cache-dir -r requirements.txt

# During debugging, this entry point will be overridden.
CMD ["gunicorn", "--bind", "0.0.0.0:3300", "app:app"]

RUN apt-get install -y g++
RUN pip install --upgrade pip

# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Change the working directory to /app/src
WORKDIR /app/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable for the port
ENV PORT=8000

# Make port available to the world outside this container
EXPOSE $PORT

# Define environment variable
ENV NAME "Knowledge Database"

# Run main.py when the container launches
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

RUN echo "deb http://deb.debian.org/debian/ bookworm main" > /etc/apt/sources.list.d/bookworm.list

# Install build essentials and gcc-11
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc-11 \
    g++-11

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Change the working directory to /app/src
WORKDIR /app/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable for the port
ENV PORT=8100

# Make port available to the world outside this container
EXPOSE $PORT

# Define environment variable
ENV NAME "Knowledge Database"

# Run main.py when the container launches
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

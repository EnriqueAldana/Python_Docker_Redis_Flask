# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Python2.7_REDIS
ENV REDIS_PORT 6379
ENV REDIS_HOST redis
ENV REDIS_DB 0

# Run app.py when the container launches
CMD ["python", "appWebServer.py"]


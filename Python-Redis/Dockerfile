# Use an official Python runtime as a parent image
FROM redis

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 6379 available to the world outside this container
EXPOSE 6379

# Define environment variable
ENV NAME PythonRedis_REDIS_SERVER
ENV REDIS_PORT 6379
ENV REDIS_HOST localhost
ENV REDIS_DB 0

# Run app.py when the container launches
RUN  ["python", "appPython2Redis.py"]


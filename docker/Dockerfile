# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY python/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the Python scripts into the container
COPY python/ /app/

# Default command to keep the container running or to run specific scripts
CMD ["/bin/bash"]

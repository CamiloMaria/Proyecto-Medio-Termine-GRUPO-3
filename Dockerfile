# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Set the entrypoint for the container
ENTRYPOINT ["python", "main.py"]

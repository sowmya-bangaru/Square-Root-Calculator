# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "-m", "unittest", "test_square_root_calculation.py"]
# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Python buffering and ensure Python output is sent directly to the terminal without buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose the port on which your Django app will run (change 8000 to the port your Django app uses)
EXPOSE 7000

# Collect static files (if needed) and run the Django development server
CMD python manage.py runserver 0.0.0.0:8000

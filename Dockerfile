# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install vim (and required tools)
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /code/

# Run the server
CMD ["bash", "-c", "python manage.py makemigrations emp_app && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

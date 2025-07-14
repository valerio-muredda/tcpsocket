# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .
COPY templates/ templates/

# Expose the port Flask-SocketIO will run on
EXPOSE 5000

# Command to run the application using Gunicorn (recommended for production)
# Gunicorn will manage the Flask app and SocketIO with eventlet workers
CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]

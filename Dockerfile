# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables for Python to not buffer output and for running Django in a production environment
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run database migrations
RUN python manage.py migrate

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

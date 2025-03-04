# Use official Python runtime
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies explicitly (to avoid caching issues)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . /app/

# Expose port (Heroku assigns a random port)
EXPOSE 5000

# Run Gunicorn to start Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

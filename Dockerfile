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

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

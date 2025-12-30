FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY echo_api.py .

# Set default environment variables for cluster info
#ENV CLUSTER_COUNTRY=XX
#ENV CLUSTER_LOCATION="Not Provided"
#ENV CLUSTER_PROVIDED_BY="Not Provided"

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "echo_api.py"]

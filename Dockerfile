FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create config directory
RUN mkdir -p config

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PMM_CONFIG_PATH=/app/config

# Expose port (if needed for web interface later)
EXPOSE 8080

# Run the application
CMD ["python", "pmm.py"]

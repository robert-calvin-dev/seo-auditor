# Base image
FROM python:3.11-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install .

# Expose reports folder (already present after COPY step)
# ENTRYPOINT remains:
 ENTRYPOINT ["seo-auditor"]


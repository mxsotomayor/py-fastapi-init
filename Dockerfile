FROM python:3.11-slim AS base

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip and uvicorn-related deps
COPY pyproject.toml .
COPY README.md . 
# optional if included in project

RUN pip install --upgrade pip \
    && pip install "uv[fastapi]"

# Install your dependencies from pyproject.toml
RUN pip install . --no-cache-dir

# Copy the app source
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

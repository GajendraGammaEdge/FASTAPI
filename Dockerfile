FROM python:3.11-slim

WORKDIR /app

# Disable poetry virtualenv creation inside Docker
ENV POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y curl gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && poetry --version

# Install debugpy for debugging
RUN pip install debugpy

# Copy project dependency files and install dependencies
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root

# Copy the full app
COPY . .

# Make wait-for-it.sh executable
RUN chmod +x wait-for-it.sh

# Expose ports for app and debug
EXPOSE 8080 5678

# Default CMD runs uvicorn with debugpy
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]




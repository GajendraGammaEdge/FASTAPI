#!/bin/bash



# Exit immediately if a command exits with a non-zero status
set -e

echo "=== Running prestart tasks ==="

# 1 Apply database migrations
# This ensures the database schema is up-to-date
# Alembic reads your migration scripts and applies them
echo "Applying database migrations..."
alembic upgrade head

# 2Create log directories if they don't exist
# Some apps write logs to files, so the folder must exist
LOG_DIR="logs"
if [ ! -d "$LOG_DIR" ]; then
  echo "Creating logs directory..."
  mkdir -p "$LOG_DIR"
fi

# 3️⃣ Environment variables check
# Optional: load environment variables from a .env file
if [ -f ".env" ]; then
  echo "Loading environment variables from .env"
  export $(grep -v '^#' .env | xargs)
fi

# 4️⃣ Any other setup tasks
# Example: check if RabbitMQ or other services are reachable
echo "Prestart tasks completed."

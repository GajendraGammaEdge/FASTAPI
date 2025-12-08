#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=== Starting GAP application ==="

# 1 Run prestart tasks first
echo "Running prestart.sh..."
./prestart.sh

# 2 Start FastAPI server with Uvicorn
# --host 0.0.0.0 allows access from any network interface (useful in Docker)
# --port 8000 sets the port
# --eload automatically reloads server on code changes (dev only)
echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 3️⃣ Optional: Start background workers
# Example for RabbitMQ consumers
# echo "Starting RabbitMQ consumer..."
# python -m app.workers.consumer

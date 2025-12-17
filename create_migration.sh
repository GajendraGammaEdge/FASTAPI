#!/bin/bash

# Script to create a new Alembic migration file
# Usage: ./create_migration.sh "description of changes"

if [ -z "$1" ]; then
    echo "Error: Please provide a migration description"
    echo "Usage: ./create_migration.sh \"description of changes\""
    exit 1
fi

echo "Creating migration: $1"
poetry run alembic revision --autogenerate -m "$1"

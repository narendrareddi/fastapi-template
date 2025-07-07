#!/usr/bin/env bash
set -e

# Wait for Postgres to be ready (uses DATABASE_URL)
echo "⏳ Waiting for Postgres at $DATABASE_URL..."
until pg_isready -q -d "$DATABASE_URL"; do
  sleep 1
done

# Run Alembic migrations
echo "🛠 Applying database migrations..."
alembic upgrade head

# Launch the FastAPI app
echo "🚀 Starting Uvicorn server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

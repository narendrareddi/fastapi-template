# Dockerfile

# ─── Builder Stage: install dependencies ───────────────────────
FROM python:3.12-slim AS builder

# Prevent .pyc creation and enable unbuffered outputs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system build deps for psycopg2 and asyncpg
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# ─── Final Stage: build runtime image ────────────────────────
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your application code
COPY . .

# Expose the port Uvicorn will run on
EXPOSE 8000

# Entrypoint script
ENTRYPOINT ["./docker-entrypoint.sh"]

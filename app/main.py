"""
Main entry point for the Async FastAPI Template application.

This module:
  - Configures structured logging for the entire app.
  - Initializes the FastAPI application with metadata.
  - Mounts API routers for each resource.
  - Exposes a simple root health-check endpoint.
"""

from fastapi import FastAPI
from app.api.routes import users  # router for user-related endpoints
from app.core.logger import setup_logging  # function to configure logging handlers/formatters

# ─── Initialize logging before app creation so all startup logs are captured ───
setup_logging()

# ─── Instantiate the FastAPI application with a descriptive title ──────────────
app = FastAPI(
    title="Async FastAPI Template",
    description="A starter template for building async FastAPI services with SQLAlchemy",
    version="1.0.0",
)

# ─── Mount the users router at /users, tag it “Users” for Swagger grouping ──────
app.include_router(
    users.router,      # the APIRouter instance from app/api/routes/users.py
    prefix="/users",   # all routes in this router will be under /users
    tags=["Users"],    # used in the auto-generated docs
)

@app.get("/")
async def root():
    """
    Root health-check endpoint.
    
    Returns a simple welcome message to verify the service is running.
    """
    return {"message": "Welcome to the Async FastAPI Template"}

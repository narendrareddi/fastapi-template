"""
Asynchronous database engine and session setup using SQLAlchemy.

This module defines:
  - `engine`: an AsyncEngine connected to the database URL from settings.
  - `AsyncSessionLocal`: a session factory for creating AsyncSession instances.
  - `get_db()`: a FastAPI dependency that yields a database session per request.

Usage in your FastAPI routes:
    @app.get("/items/")
    async def read_items(db: AsyncSession = Depends(get_db)):
        # use `db` for async queries
        ...
"""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # DATABASE_URL is loaded from env/config

# Create the SQLAlchemy async engine
#  - settings.DATABASE_URL: connection string (e.g. postgresql+asyncpg://…)
#  - future=True: enable 2.0 style API
#  - echo=False: disable SQL statement logging (set True to debug)
engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=False,
)

# Configure a sessionmaker bound to the async engine
#  - class_=AsyncSession: produces AsyncSession objects
#  - expire_on_commit=False: objects won't be expired after commit
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    """
    FastAPI dependency that provides a transactional AsyncSession.

    Yields:
        AsyncSession: an async DB session bound to our engine.

    Ensures:
        - the session is properly closed/cleaned up after each request,
        - any uncommitted changes are rolled back if an exception occurs.
    """
    # Create a new session instance
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            # Context manager ensures session.close() is called here
            pass

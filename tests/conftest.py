# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.base import Base
from app.core.config import settings

# 1) Use your sync DB URL (psycopg) to manage schema
engine = create_engine(settings.ALEMBIC_URL, echo=False)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 2) Drop + create tables once per pytest session
@pytest.fixture(scope="session", autouse=True)
def initialize_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# 3) Provide a TestClient for your tests
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

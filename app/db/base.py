# app/db/base.py

"""
Model registry for Alembic autogeneration.

This module’s sole job is to:
  1. Import every ORM model class so that SQLAlchemy’s MetaData
     (Base.metadata) “knows about” all tables.
  2. Expose that Base.metadata to Alembic’s env.py via:

        from app.db.base import Base
        target_metadata = Base.metadata

Without importing each model here, Alembic’s `--autogenerate`
would not see your models and thus wouldn’t include them in migrations.
"""

# Import the declarative base (so Base.metadata is available)
from app.db.base_class import Base

# Import each model class so it registers itself on Base.metadata
from app.db.models.user import User
# from app.db.models.item import Item
# from app.db.models.order import Order
# …and so on for every model in your app…

# app/db/base_class.py

"""
Defines the foundational DeclarativeBase subclass that all ORM models inherit from.

By centralizing the base class here, you can:
  - Apply common configuration (e.g. naming conventions) in one place
  - Avoid circular imports, since no models are imported here
  - Keep your model definitions clean and focused on columns/relationships
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    Usage:
        from app.db.base_class import Base

        class User(Base):
            __tablename__ = "users"
            id = Column(Integer, primary_key=True, index=True)
            # ...
    """
    # ✏️ Add any shared ORM configuration here (e.g. __table_args__, naming conventions)
    pass

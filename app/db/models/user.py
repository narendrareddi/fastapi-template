from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class User(Base):
    """
    SQLAlchemy ORM model for the 'temp_users' table in the 'test' schema.

    Attributes:
        id (int): Primary key for the user.
        name (str): Name of the user.
        email (str): Unique email address of the user.
    """
    __tablename__ = "temp_users"  # Table name in the database
    __table_args__ = {"schema": "test"}  # Schema name

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each user
    name = Column(String, index=True)  # User's name, indexed for faster search
    email = Column(String, unique=True, index=True)  # User's email, must be unique and indexed

"""
API routes for user-related operations.

This module defines endpoints for creating a new user and retrieving all users.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.schemas.user import UserCreate, UserOut
from app.db.session import get_db
from app.db.curd.user import create_user, get_users

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new user.

    Args:
        user (UserCreate): The user data to create.
        db (AsyncSession): The database session dependency.

    Returns:
        UserOut: The created user.
    """
    # Call the create_user function to add a new user to the database
    return await create_user(db, user)

@router.get("/", response_model=list[UserOut])
async def read_users(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all users.

    Args:
        db (AsyncSession): The database session dependency.

    Returns:
        list[UserOut]: A list of all users.
    """
    # Call the get_users function to fetch all users from the database
    return await get_users(db)

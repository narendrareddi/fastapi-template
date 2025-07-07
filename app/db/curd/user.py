import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User
from app.db.schemas.user import UserCreate

logger = logging.getLogger(__name__)

async def create_user(db: AsyncSession, user: UserCreate):
    """
    Create a new user in the database.

    Args:
        db (AsyncSession): The async database session.
        user (UserCreate): The user data to create.

    Returns:
        User: The created user instance.
    """
    logger.info(f"Creating user: {user.email}")
    # Create a new User ORM instance
    user = User(name=user.name, email=user.email)
    db.add(user)  # Add the user to the session
    await db.commit()  # Commit the transaction
    await db.refresh(user)  # Refresh to get updated user data (e.g., id)
    return user

async def get_users(db: AsyncSession):
    """
    Retrieve all users from the database.

    Args:
        db (AsyncSession): The async database session.

    Returns:
        List[User]: A list of user instances.
    """
    # Execute a SELECT query for all User records
    result = await db.execute(select(User))
    return result.scalars().all()  # Return all user objects

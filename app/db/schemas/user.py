from pydantic import BaseModel, ConfigDict

# Schema for creating a new user
class UserCreate(BaseModel):
    """
    Schema for user creation input.
    """
    name: str  # User's name
    email: str  # User's email address

# Schema for outputting user data, including the user ID
class UserOut(UserCreate):
    """
    Schema for user output with ID.
    Inherits name and email from UserCreate.
    """
    id: int  # Unique identifier for the user

    # Enable model config to allow population from ORM objects
    model_config = ConfigDict(from_attributes=True)

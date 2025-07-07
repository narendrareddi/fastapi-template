from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cached_property

class Settings(BaseSettings):
    """Settings configuration for the FastAPI application.
    This class loads application settings from environment variables or a .env file,
    and provides properties to assemble database connection URLs.
        DB_USER (str): Database username.
        DB_PASSWORD (str): Database password.
        DB_HOST (str): Database host address.
        DB_PORT (int): Database port number.
        DB_NAME (str): Database name.
    Properties:
        DATABASE_URL (str): Assembled SQLAlchemy async database URL using asyncpg driver.
        ALEMBIC_URL (str): Assembled SQLAlchemy sync database URL using psycopg driver.
    """
    # Specify the .env file to load environment variables from
    model_config = SettingsConfigDict(env_file="config/dev.env")

    DB_USER:     str
    DB_PASSWORD: str
    DB_HOST:     str
    DB_PORT:     int
    DB_NAME:     str
    APP_ENV:     str = "dev"
    
    @cached_property
    def DATABASE_URL(self) -> str:
        """
        Assemble the full SQLAlchemy URL from individual pieces.
        """
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )
        
    @cached_property
    def ALEMBIC_URL(self) -> str:
        """
        Assemble the full SQLAlchemy URL from individual pieces.
        """
        return (
            f"postgresql+psycopg://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )

# Instantiate the settings object to be used throughout the app
settings = Settings()

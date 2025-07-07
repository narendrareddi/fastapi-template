from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Import application settings, including database URLs and other config values
from app.core.config import settings 

# Import the SQLAlchemy Base class, which holds the metadata for all models
from app.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the SQLAlchemy URL from application settings (overrides .ini file)
config.set_main_option("sqlalchemy.url", settings.ALEMBIC_URL)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# Set target_metadata to the Base metadata for autogeneration support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def include_name_test_file(obj, name, type_, reflected, compare_to):
    """
    Determines whether a database object should be included in Alembic migrations based on its type and schema.

    Args:
        obj: The database object being considered (e.g., a Table object).
        name (str): The name of the object.
        type_ (str): The type of the object (e.g., "table").
        reflected (bool): Whether the object was reflected from the database.
        compare_to: The object being compared to, if any.

    Returns:
        bool: True if the object should be included; False otherwise. Only includes tables in the "test" schema.
    """
    if type_ == "table" and obj.schema != "test":
        return False
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    version_table_schema="test",  #schema name
    version_table="alembic_version_test_file",  #  different table in schema
    include_schemas=True, #Schema fileter allow
    include_object=include_name_test_file # schema checks
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,version_table="alembic_version_test_file",  # 👈 different table
    version_table_schema="test", include_schemas=True,
    include_object=include_name_test_file
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.db_configuration import Base  # Make sure this imports your SQLAlchemy Base
import app.model  # Ensure models are imported so metadata is registered

# Alembic target metadata
target_metadata = Base.metadata

# Load Alembic config
config = context.config
fileConfig(config.config_file_name)

# Use DATABASE_URL environment variable if set (Docker-friendly)
DATABASE_URL = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))

def run_migrations_online():
    """Run migrations in 'online' mode."""

    config = context.config
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Detect column type changes
        )

        with context.begin_transaction():
            context.run_migrations()

# Run migrations
run_migrations_online()

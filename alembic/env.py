import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from logging.config import fileConfig

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.db_configuration import Base
import app.model

target_metadata = Base.metadata
config = context.config
fileConfig(config.config_file_name)

DATABASE_URL = os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url"))

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=DATABASE_URL
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()

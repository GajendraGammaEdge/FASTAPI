# Database Migration Workflow

This project uses Alembic for database migrations.

## How It Works

1. **Manual Migration Creation**: Migration files are created manually when you run a command
2. **Automatic Migration Application**: When you run `docker-compose up`, all migrations are automatically applied to the database
3. **Fresh Database**: When you run `docker-compose down -v` and then `docker-compose up`, all migrations are applied from scratch

## Creating a Migration

### Method 1: Using the Helper Script (Recommended)

```bash
./create_migration.sh "description of your changes"
```

### Method 2: Using Poetry Directly

```bash
poetry run alembic revision --autogenerate -m "description of your changes"
```

### Method 3: Using Docker

```bash
docker-compose run --rm alembic poetry run alembic revision --autogenerate -m "description of your changes"
```

## How Migrations Are Applied

When you run `docker-compose up`:

1. The `db` service starts the PostgreSQL database
2. The `alembic` service waits for the database to be healthy
3. The `alembic` service automatically runs `alembic upgrade head` to apply all pending migrations
4. The `app` service starts only after migrations are successfully applied

## Common Commands

### View Migration History
```bash
poetry run alembic history
```

### View Current Revision
```bash
poetry run alembic current
```

### Upgrade to Latest Migration
```bash
poetry run alembic upgrade head
```

### Downgrade One Migration
```bash
poetry run alembic downgrade -1
```

### Create Empty Migration (for custom SQL)
```bash
poetry run alembic revision -m "description"
```

## Workflow Example

1. **Make changes to your models** (e.g., in `app/model/genai_chat.py`)
2. **Create migration file**:
   ```bash
   ./create_migration.sh "add new column to chat_sessions"
   ```
3. **Review the generated migration** in `alembic/versions/`
4. **Test the migration**:
   ```bash
   docker-compose down -v
   docker-compose up
   ```
5. **Commit the migration file** to version control

## Important Notes

- Migration files are located in `alembic/versions/`
- Always review auto-generated migrations before applying them
- Never modify already-applied migrations; create a new one instead
- The database is automatically updated only when migrations run, not when the app starts

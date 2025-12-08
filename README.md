
`sudo docker compose up`

##### Now you are setup is ready, your database is will be autometically created and data with upgraded with latest migrated files.

## Executing Create Migration Script Commands Inside the Container
- sudo docker exec myapp-api poetry run alembic upgrade head

- sudo docker exec myapp-api poetry run alembic revision --autogenerate -m "first_migration"


# Run migration locally
## Create a Virtual Environment
Set up a Python virtual environment right within the project directory using Poetry. This keeps all project-related packages contained.

1.  Open a second terminal window or tab and navigate to the /api directory again

2. `poetry config virtualenvs.in-project true`

3. `poetry install`

4. `poetry shell`

## Database Migrations
Run the migration command to apply database changes:

`poetry run alembic upgrade head`

## Creating Migration Scripts
If you need to create new migration scripts based on changes to the database models, use the following command. Replace "first migration" with a suitable name for your migration.

`poetry run alembic revision --autogenerate -m "first migration"`

## Run pytest
1. Enter Docker Container: `docker exec -it <container-id> bash`
2. Run: `poetry run pytest`
3. Run particular file: `poetry run pytest app/tests/unit/test_access_control.py`
4. Run unit test inside container without going inside it: `sudo docker exec myapp-api poetry run pytest app/tests/unit`

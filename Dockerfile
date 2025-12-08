FROM python:3.11-slim

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="/root/.local/bin:$PATH" && \
    /root/.local/bin/poetry --version

COPY pyproject.toml poetry.lock* /app/
RUN pip install alembic 

RUN /root/.local/bin/poetry install --no-root

COPY . .

EXPOSE 8080

CMD ["/root/.local/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

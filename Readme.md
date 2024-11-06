# Yields Data Pipeline

## Overview

This project aims to create a data pipeline for yield farming data from the [Yields API](https://yields.llama.fi/).

## Terminal Commands

### Install dependencies

```bash
pipenv install
```

### Run black to format the code

```bash
pipenv run black
```

### starting pipenv shell

```bash
pipenv shell
```

### Run the pipeline

```bash
pipenv run python -m pipeline
```

## Docker- to start the postgres container

```bash
docker compose up
```

## Postgres- to access the postgres container

```bash
docker exec -it postgres psql -U dbuser -d mydb
```

## To stop the postgres container

```bash
docker compose down
```


### Initialize Alembic

```bash
alembic init migrations
```

### Create initial migration
```bash
alembic revision --autogenerate -m "Create pools and pools_historical tables"
```

### Apply migration

```bash
alembic upgrade head
```






## Repo Structure

your_project/
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py         # Contains Base model and common configurations
│   │   ├── mixins.py       # Common model mixins (e.g., TimestampMixin)
│   │   ├── pools.py        # Pool model
│   │   └── pools_historical.py  # PoolHistorical model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── pools.py        # Pydantic models for validation
│   ├── database.py         # Database connection handling
│   └── config.py          # Configuration settings
├── migrations/
│   └── env.py
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md

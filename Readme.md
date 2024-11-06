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

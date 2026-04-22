# GigaAcademy Mentees CRUD — Starter Repo

Week 5 homework. Build a Python CLI that manages GigaAcademy mentees in a PostgreSQL database running in Docker.

Read the full brief your mentor shared before starting.

## Prerequisites

- Docker Desktop (or Docker Engine) — `docker --version`
- Python 3.11 or newer — `python3 --version`

## Setup

```bash
# 1. Copy env file
cp .env.example .env

# 2. Start the database
docker compose up -d

# 3. Confirm it's running
docker ps

# 4. Create virtual env and install deps
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 5. Seed the DB (optional, once container is healthy)
docker exec -i giga_mentees_db psql -U giga -d giga_mentees < sql/seed.sql

# 6. Run the app
python app.py
```

## Stopping / tearing down

```bash
docker compose down           # stop the container, keep data
docker compose down -v        # also wipe the data volume (fresh start)
```

## What you need to implement

Open `app.py`. All functions marked `NotImplementedError` are yours.

For **Level 1**: fill in the four CRUD functions and `run_menu()`.

For **Level 2**: see the hints at the bottom of `app.py` and the brief.

## Your submission README

Before submitting, **replace this README** with one that covers:

1. Setup steps (you can keep the ones above).
2. How to run the app.
3. Which level you completed (Level 1 only, or Level 1 + Level 2).
4. A short "What was hard" section — 3 to 5 honest sentences.

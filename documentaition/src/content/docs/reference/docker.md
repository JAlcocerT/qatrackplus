---
title: "Docker Deployment"
description: "Running QATrack+ with Docker Compose using the provided configuration."
---

# QATrack+ Docker Setup

This guide describes how to run QATrack+ using Docker and Docker Compose, leveraging the files in `deploy/docker/`.

## Prerequisites

- Docker Engine ≥ 19.03
- Docker Compose ≥ 1.27
- Minimum 2 GB RAM
- Ports 80/443 (nginx) and 8000 (Django) available

## Directory Layout (`deploy/docker/`)

- **docker-compose.yml**: defines three services:
  - `qatrack-nginx`: Nginx front‐end
  - `qatrack-django`: Django+Gunicorn app
  - `qatrack-postgres`: PostgreSQL database
- **django/Dockerfile**: base image with Python 3.6, OS deps (cron, postgresql-client, chromium)
- **init.sh**: entrypoint to install Python deps, run migrations, setup cron, and launch Gunicorn
- **nginx.conf**: Nginx proxy config for static/media and upstream to Gunicorn
- **cron_backup.sh** & **crontab**: backup scripts and schedule
- **docker_initialisation.py** & **docker_utilities.py**:
  - seed initial data
  - perform backup/restore hooks

## Quick Start

From the project root:

```bash
cd deploy/docker
docker-compose up --build -d
```

This will:

1. Build the `qatrack-django` image from `django/Dockerfile`.
2. Start `qatrack-postgres` and initialize the database volume.
3. Mount the project code into the Django container.
4. Run `init.sh`, which:
   - Starts cron
   - Creates a Python virtualenv and installs `requirements/docker.txt`
   - Runs backup/restore (if user-data present)
   - Loads initial data via `docker_initialisation.py`
   - Applies Django migrations and creates cache table
   - Installs cron jobs for daily backups
   - Launches Gunicorn on port 8000
5. Start Nginx on ports 80 and 443, serving static files and proxying to Gunicorn.

## Configuration

- **Settings override**: `qatrack/docker_settings.py`:
  - `ALLOWED_HOSTS = ['*']`
  - Generates or reads `SECRET_KEY` at `deploy/docker/user-data/secret_key.txt`
  - Configures PostgreSQL at host `qatrack-postgres`, user/password `postgres`
- **Custom settings**: mount a `local_settings.py` into the code volume or set environment variables in a `docker-compose.override.yml`.

## Data Persistence

- **Postgres data**: persisted in a named volume `qatrack-postgres-volume`.
- **Static files**: served directly from `qatrack/static/` in the project repository.
- **Media uploads**: stored in the `qatrack/media` directory and mounted into both Django and Nginx.
- **Backups & secrets**: under `deploy/docker/user-data/`.

## Logs & Monitoring

- View Django logs:
  ```bash
  docker-compose logs -f qatrack-django
  ```
- View Nginx logs:
  ```bash
  docker-compose logs -f qatrack-nginx
  ```
- Cron-job backups run daily per `crontab` configuration.

## Shutdown & Cleanup

```bash
cd deploy/docker
docker-compose down
# To remove database volume:
docker volume rm deploy/docker_qatrack-postgres-volume
```

---

With this setup, you should have a fully functional QATrack+ instance running in Docker. Adjust ports, volume mounts, or environment variables in `docker-compose.override.yml` as needed for your environment.
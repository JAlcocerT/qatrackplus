---
title: "Deployment Guide"
description: "How to install, configure, and deploy QATrack+ in various environments."
---

# Deployment

## Prerequisites

- Python 3.6+  
- Database: SQLite (dev) / PostgreSQL / MySQL  
- Web server: Apache (mod_wsgi) / Gunicorn behind Nginx  
- Redis or supporting django-q broker

## Environment Setup

1. Clone repository:
   ```bash
   git clone https://github.com/qatrackplus/qatrackplus.git
   cd qatrackplus
   ```
2. Create virtualenv & install:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements/base.txt
   ```
3. Configure `qatrack/local_settings.py` (see `qatrack/docker_settings.py` for Docker hints).

## Database Migrations & Static Files

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## Web Server Examples

### Docker

- See `deploy/docker/` for `Dockerfile` and `docker-compose.yml` examples.

### Apache (mod_wsgi)

- Templates in `deploy/apache/`:  
  - `qatrack.conf` for virtual host  
  - WSGI entry at `/qatrack/wsgi.py`

### Supervisor

- `deploy/supervisor/` contains sample `.conf` for `gunicorn` and `django-q` workers.

### Windows

- Guidance in `deploy/win/`, using IIS or Windows services.

## Running Tasks

- Scheduler:
  ```bash
  python manage.py qatrack_schedule_reports
  ```
- Background Workers:
  ```bash
  python manage.py qcluster
  ```
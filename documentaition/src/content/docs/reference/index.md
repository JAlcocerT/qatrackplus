---
title: "QATrack+ Project Overview"
description: "High-level summary of the QATrack+ LIMS and QA tracking system, its architecture, and dependencies."
---

# QATrack+

QATrack+ is an open-source, Django-based Laboratory Information Management System (LIMS) for tracking Quality Assurance (QA) of equipment and processes. It supports:

- **QA Test Management**: define tests, test lists, and execute QA sessions.
- **Service Log**: schedule, record, and review equipment service events.
- **Parts & Units Inventory**: manage parts, manufacturers, models, and laboratory units.
- **User Accounts & Authentication**: local and Active Directory integration.
- **REST API**: full-featured API (based on Django REST Framework) to integrate with other systems.
- **Reporting & Scheduling**: generate, schedule, and email PDF/Excel reports.
- **Attachments & Notifications**: upload files against records and receive email alerts.
- **Issue Tracking & Faults**: record faults, review status, and generate follow-up actions.

---

## Directory Structure

```
./
├── qatrack/                   # Django project & apps
│   ├── accounts/             # User auth & AD integration
│   ├── api/                  # REST API endpoints
│   ├── qatrack_core/         # Core utilities, mixins, tasks
│   ├── qa/                   # QA test definitions & sessions
│   ├── service_log/          # Equipment service events
│   ├── reports/              # Reporting & scheduling engine
│   ├── parts/                # Parts catalog
│   ├── units/                # Laboratory units & availability
│   └── settings.py, urls.py, wsgi.py, … 
├── docs/                      # Sphinx source (legacy)
├── documentaition/            # Astro site scaffold
└── requirements/              # Environment dependency files
```

---

## Core Modules

- **Accounts** (`accounts.md`): Authentication, Active Directory, user/group mapping.
- **API** (`api.md`): JSON REST endpoints for all major models.
- **Core** (`core.md`): Shared utilities, scheduling, PDF generation.
- **QA** (`qa.md`): Test definitions, test lists, sessions, and results.
- **Service Log** (`service-log.md`): Event templates, logging, statuses.
- **Reports** (`reports.md`): Scheduled and on-demand PDF/Excel reporting.
- **Parts** (`parts.md`): Parts catalog, part types, manufacturers.
- **Units** (`units.md`): Equipment units, availability calendars.

---

## Dependencies

- **Python**: 3.6+ (tested with 3.7–3.9)
- **Django**: 2.2.18
- **django-q**: 1.3.4 (background task scheduling)
- **Django REST Framework**: 3.12.2
- **Third-party Django apps**: django-recurrence, django-mptt, django-sql-explorer, etc.
- **Scientific libraries**: numpy, scipy, matplotlib, pandas, openpyxl, reportlab, pylinac-qatrackplus
- **Testing**: pytest, pytest-django, coverage

See `requirements/base.txt` and environment-specific files in `requirements/`.

---

## Configuration & Environment

- **Local Settings**: Create `qatrack/local_settings.py` or use `.env` file to override `settings.py`.
- **Database**: Supports SQLite, PostgreSQL, MySQL (see `deploy/` templates).
- **Static & Media**: Configure `STATIC_ROOT`, `MEDIA_ROOT` in settings.
- **Migrations**:  
  ```bash
  python manage.py migrate
  ```
- **Collect Static**:  
  ```bash
  python manage.py collectstatic
  ```
- **Development Server**:  
  ```bash
  python manage.py runserver
  ```
- **Tests**:  
  ```bash
  ./runtests.sh
  ```

---

## Static Analysis & Tooling

- **Code Formatting**: `black`
- **Linting**: `flake8`, `pep8`
- **Pre-commit**: configured in `.pre-commit-config.yaml`
- **Documentation**: Legacy Sphinx under `docs/`, new Astro site under `documentaition/`.

```bash
pre-commit run --all-files
```
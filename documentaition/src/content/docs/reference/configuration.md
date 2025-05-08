---
title: "Configuration & Settings"
description: "Configuration files and environment settings for QATrack+"
---

# Configuration & Settings

This document describes the key configuration files and environment settings for QATrack+.

## manage.py
- Entry point for Django management commands.
- Usage: `python manage.py <command> [options]`.

## qatrack/settings.py
- Default project settings.
- Sections include:
  - `DEBUG`, `ADMINS`, `DATABASES`
  - Time zone, localization (`TIME_ZONE`, `USE_TZ`)
  - Media and static file settings (`MEDIA_ROOT`, `STATIC_ROOT`)
  - Installed apps and middleware
  - Template and context processor configuration

## qatrack/local_settings.py
- Override `settings.py` values for site-specific customization.
- Not version-controlled; create from sample or provide your own.

## qatrack/docker_settings.py
- Overrides for Docker deployments:
  - Sets `ALLOWED_HOSTS` to `['*']`.
  - Reads or generates `SECRET_KEY` at `deploy/docker/user-data/secret_key.txt`.
  - Configures PostgreSQL database (`postgres` service).

## qatrack/test_settings.py
- Overrides for CI and testing:
  - Disables notifications, uses a simple password hasher.
  - Configures `AUTHENTICATION_BACKENDS` for test accounts.
  - Can import additional overrides from `local_test_settings.py`.

## Environment Variables & .env
- Common variables:
  - `SECRET_KEY`: Django secret key
  - Database credentials (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, etc.)
  - `DEBUG`: Enable/disable debug mode
  - ADFS and authentication settings (`ADFS_*`)
- Use a `.env` file in the project root for local development.

## Configuration Best Practices
- Keep secret keys and credentials out of version control.
- Use `local_settings.py` for environment-specific settings.
- Validate settings in CI by running `python manage.py check`.
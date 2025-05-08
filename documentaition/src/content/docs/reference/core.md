---
title: "Core Module"
description: "Shared utilities, mixins, scheduling, and template tags."
---

# Core (`qatrack/qatrack_core`)

Provides generic building blocks used by all apps.

## Utilities (`utils.py`)

- `chrometopdf(html: str, name: str = "") -> bytes`  
  Renders HTML to PDF via headless Chrome.

- Date helpers:  
  - `start_of_day(dt: datetime)`, `end_of_day(dt: datetime)`  
  - `today_start()`, `today_end()`, `today_start_end()`  
  - `relative_dates(date_range: str, pivot: datetime=None)`  
    Compute intervals like "next 7 days", "last month".

## Mixins (`mixins.py`)

- Reusable class-based view mixins for permission checks, pagination, JSON export.

## Tasks (`tasks.py`)

- Background jobs (via django-q) for report scheduling, email dispatch.

## Forms & Widgets

- Custom form fields (`fields.py`), widgets (`widgets.py`), and form utilities.

## Views & Serializers

- Shared API serializers (`serializers.py`) and generic CBVs (`views.py`).

## Scheduling (`scheduling.py`)

- Tools to register recurring tasks, schedule reports and reminders.
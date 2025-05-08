---
title: "Reports Module"
description: "On-demand and scheduled PDF/Excel report generation."
---

# Reports (`qatrack/reports`)

Enables flexible reporting over QA, service logs, equipment, and faults.

## Models (`models.py`)

- **ScheduledReport**  
  Configuration for recurring reports (cron, filters).

- **ScheduledReportFilter**  
  Stores filter criteria (date ranges, units, statuses).

## Filters & Forms

- `filters.py`: Django-filter classes for report criteria.
- `forms.py`: Form definitions for interactive report parameter entry.

## Views & Tasks

- `views.py`: Render and preview reports in-browser.
- `tasks.py`: Queue PDF/Excel generation jobs via django-q.

## Built-in Reports

- Equipment status, upcoming QA, fault trends, service events, custom SQL Explorer.

## Usage

```bash
python manage.py qatrack_schedule_reports
```
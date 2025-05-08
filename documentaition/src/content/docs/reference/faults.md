---
title: "Faults Module"
description: "Fault logging and review workflows"
---

# Faults Module (`qatrack.faults`)

The Faults module allows users to report, review, and acknowledge equipment faults.

## Key Components

- **models.py**:
  - `Fault`: Represents a reported fault with description and status.
  - `FaultType`: Categorizes faults; codes must be unique.
- **views.py**: Views for submitting and reviewing faults.
- **forms.py**: Forms for fault submission and filtering.
- **urls.py**: URL patterns under `/faults/`.
- **signals**: Cache invalidation on fault changes.

## Usage Examples

```bash
# Report a new fault:
POST /faults/report/ { unit: 2, description: "Temperature out-of-range" }

# Review unacknowledged faults:
GET /faults/unreviewed/
```
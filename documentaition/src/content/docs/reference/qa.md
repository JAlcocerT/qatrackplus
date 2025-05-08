---
title: "QA Module"
description: "Definitions and execution of Quality Assurance tests and test lists."
---

# QA (`qatrack/qa`)

Handles creation of QA tests, test lists, and recording of test sessions.

## Models (`models.py`)

- **Test**  
  Definition of a single QA test (name, description, limits, units).

- **TestList**  
  Group of Tests to be run together, with frequency rules (via django-recurrence).

- **TestListInstance**  
  Scheduled occurrence of a TestList.

- **TestInstance**  
  Execution record of a single Test within a TestListInstance.

## Views & URLs

- `/qa/tests/`, `/qa/lists/`, `/qa/sessions/` for listing, creating, and reviewing.

## Utilities

- Control charts (`control_chart/`) for trending test data.
- `testpack.py` to bundle and download test PDFs.

## Example

```python
from qa.models import Test, TestList, TestListInstance

# Create a new QA session
tlist = TestList.objects.get(pk=1)
session = tlist.schedule_next()
```
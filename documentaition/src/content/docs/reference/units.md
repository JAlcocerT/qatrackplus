---
title: "Units Module"
description: "Laboratory equipment units and availability schedules."
---

# Units (`qatrack/units`)

Tracks physical lab units, their availability, and assignments.

## Models

- **Unit**: Equipment entry (name, location, serial).
- **UnitAvailableTime**: Recurring availability windows.
- **UnitTestCollection**: Group of tests assigned to a unit.

## Views & Forms

- Calendar views of upcoming QA sessions.
- Assignment pages for linking test lists to units.

## Example

```python
from units.models import Unit, UnitAvailableTime

# Get today's available units
today = date.today()
units = Unit.objects.filter(
    available_times__day_of_week=today.weekday()
)
```
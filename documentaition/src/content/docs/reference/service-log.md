---
title: "Service Log Module"
description: "Scheduling and recording of equipment service events."
---

# Service Log (`qatrack/service_log`)

Tracks maintenance and service events for lab units.

## Models (`models.py`)

- **ServiceEventTemplate**  
  Predefined template for routine service (fields, default values).

- **ServiceEvent**  
  Actual service record logged against a Unit.

- **ServiceType**, **ServiceLevel**, **Status**  
  Lookup tables for classifying events.

## Forms & Views

- `forms.py`: Entry forms for new service events.
- `views.py` & `urls.py`: CRUD interfaces and calendar views.

## Signals

- Auto-create default statuses and link templates on initialization.

## Example

```python
from service_log.models import ServiceEvent, ServiceEventTemplate

template = ServiceEventTemplate.objects.get(name="Quarterly Inspection")
event = template.create_event(unit=my_unit, performed_by=request.user)
```
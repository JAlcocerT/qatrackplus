---
title: "Parts Module"
description: "Management of parts, manufacturers, and part types."
---

# Parts (`qatrack/parts`)

Catalog of parts used in QA tests.

## Models

- **Manufacturer**: Name, website, contact.
- **PartType**: Category or family of parts.
- **Part**: Specific part record (serial number, location).

## Admin & Views

- CRUD interfaces under `/parts/`.
- Inline filtering by room, type, manufacturer.

## Example

```python
from parts.models import Part

# Filter by manufacturer
parts = Part.objects.filter(manufacturer__name="ACME")
```
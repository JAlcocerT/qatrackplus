---
title: "API Module"
description: "REST API endpoints (Django REST Framework) for all core models."
---

# API (`qatrack/api`)

Exposes JSON endpoints for programmatic access and integration.

## Structure

- **serializers.py**  
  Defines `ModelSerializer` subclasses for attachments, faults, QA, service_log, units, etc.

- **viewsets.py**  
  `ViewSet` definitions that bundle `queryset`, `serializer_class`, and permissions.

- **urls.py**  
  Registers routes under `/api/`, e.g. `/api/units/`, `/api/qa/sessions/`.

- **filters.py**  
  DRF filters to support query parameters (date ranges, status, etc.)

- **schemas.py**  
  OpenAPI schema generation.

- **apps/** subfolders  
  Separate modules for attachments, comments, contenttypes, parts, qa, service_log, units.

## Example Request

```bash
curl -X GET "https://yourserver/api/qa/sessions/?unit=5" \
     -H "Authorization: Token <your_api_key>"
```

## Key Endpoints

| Resource                 | Endpoint                        | Description                        |
|--------------------------|---------------------------------|------------------------------------|
| Units                    | `/api/units/`                   | List & detail of lab equipment     |
| QA Sessions              | `/api/qa/sessions/`             | Create and retrieve QA runs        |
| Service Events           | `/api/service_log/`             | Log and review service events      |
| Attachments              | `/api/attachments/`             | Upload/download file attachments   |
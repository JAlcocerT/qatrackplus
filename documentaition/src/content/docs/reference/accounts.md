---
title: "Accounts Module"
description: "User authentication, authorization, and Active Directory integration."
---

# Accounts (`qatrack/accounts`)

Manages user login, group assignment, and external directory (AD/LDAP) integration.

## Key Components

- **models.py**  
  - `ActiveDirectoryGroupMap(ad_group: str, groups: ManyToMany[Group], account_qualifier: bool)`  
    Maps AD groups → QATrack+ groups.  
    • `group_map() -> Dict[str, List[Group]]`  
    • `qualified_ad_group_names() -> List[str]`  

  - `DefaultGroup(group: ForeignKey[Group])`  
    Defines groups automatically assigned to new users.

- **backends.py**  
  Custom Django auth backends, e.g. `ActiveDirectoryBackend`, extending `ModelBackend`.

- **forms.py**  
  Extended login forms supporting AD lookup, password reset.

- **views.py** & **urls.py**  
  Login, logout, password change, profile endpoints.

- **utils.py**  
  Helper functions to sync AD users, group lookup.

## Usage Example

```python
from accounts.models import ActiveDirectoryGroupMap

# Fetch mapping of AD group names to QATrack+ groups
mapping = ActiveDirectoryGroupMap.group_map()
```
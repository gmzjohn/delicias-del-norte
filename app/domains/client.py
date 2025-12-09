from datetime import datetime, timezone
from .base_entity import BaseEntity

class Client(BaseEntity):
    def __init__(
        self,
        name: str,
        phone: str,
        email: str | None = None,
        description: str | None = None,
    ):
        super().__init__(id=id, status=status, created_by=created_by, updated_by=updated_by, created_at=created_at, updated_at=updated_at)

        self.name = name
        self.phone = phone
        self.status = status
        self.email = email
        self.description = description

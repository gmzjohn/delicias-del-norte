from abc import ABC
from datetime import datetime, timezone
from .enums.entity_status import EntityStatus

class BaseEntity(ABC):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.status = status
        self.created_by = created_by
        self.updated_by = updated_by
        self.created_at = created_at
        self.updated_at = updated_at

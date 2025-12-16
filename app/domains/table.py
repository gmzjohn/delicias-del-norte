from .base_entity import BaseEntity
from .enums.table_status import TableStatus

class Table(BaseEntity):
    def __init__(
        self,
        name: str,
        capacity: int,
        table_status: TableStatus,
        description: str,
    ):
        super().__init__(id=id, status=status, created_by=created_by, updated_by=updated_by, created_at=created_at, updated_at=updated_at)
        
        self.name = name
        self.capacity = capacity
        self.table_status = table_status
        self.description = description

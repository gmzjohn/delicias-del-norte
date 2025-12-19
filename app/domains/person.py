from abc import ABC
from .base_entity import BaseEntity

class Person(BaseEntity, ABC):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        firstName: str,
        lastName: str,
        address: str | None,
        email: str | None,
        phone: str | None,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by, 
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )
        
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.email = email
        self.phone = phone

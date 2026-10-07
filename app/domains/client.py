from datetime import datetime

from .enums.entity_status import EntityStatus
from .person import Person


class Client(Person):
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
        description: str | None = None,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            firstName=firstName,
            lastName=lastName,
            address=address,
            email=email,
            phone=phone,
        )
        self.description = description

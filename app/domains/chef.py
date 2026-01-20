from datetime import datetime

from app.domains.enums.employee_role import EmployeeRole

from .employee import Employee
from .enums.entity_status import EntityStatus


class Chef(Employee):
    def __init__(
        self,
        id: int,
        status: EntityStatus,
        created_by: int,
        updated_by: int,
        created_at: datetime,
        updated_at: datetime,
        first_name: str,
        last_name: str,
        address: str | None,
        email: str | None,
        phone: str | None,
        experience_years: int,
    ):
        super().__init__(
            id=id,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            first_name=first_name,
            last_name=last_name,
            address=address,
            email=email,
            phone=phone,
            role=EmployeeRole.CHEF,
        )

        self.experience_years = experience_years

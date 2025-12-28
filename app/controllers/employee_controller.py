import uuid
from datetime import datetime, timezone
from app.domains.employee import Employee
from app.domains.enums.employee_role import EmployeeRole
from app.domains.enums.entity_status import EntityStatus 

class EmployeeController:
    def create_employee(
        self,
        first_name: str, 
        last_name: str, 
        role: EmployeeRole, 
        created_by_user_id: int,
        address: str = None,
        email: str = None,
        phone: str = None
    ) -> Employee:
        random_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc)
        
        new_employee = Employee(
            id=random_id,
            status=EntityStatus.ACTIVE,
            created_by=created_by_user_id,
            updated_by=created_by_user_id,
            created_at=now,
            updated_at=now,
            first_name=first_name,
            last_name=last_name,
            address=address,
            email=email,
            phone=phone,
            role=role
        )

        return new_employee

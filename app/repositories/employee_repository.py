from collections.abc import Callable
from datetime import datetime
from typing import Any

from app.domains.employee import Employee
from app.domains.enums.entity_status import EntityStatus


class EmployeeRepository:
    def __init__(self) -> None:
        self._current_id: int = 0
        self._db: dict[int, Employee] = {}

    def get_employee(self, employee_id: int) -> Employee:
        employee = self._db.get(employee_id)

        if employee is None:
            raise ValueError("This employee does not exist")

        if employee.status == EntityStatus.INACTIVE:
            raise ValueError("This employee is currently inactive")

        return employee

    def save(self, employee: Employee) -> Employee:
        employee.id = self._current_id
        employee.status = EntityStatus.ACTIVE
        employee.created_at = datetime.now()
        employee.updated_at = datetime.now()

        self._db[self._current_id] = employee

        self._generate_next_id()

        return employee

    def delete(self, employee_id: int) -> None:
        self.update(employee_id, "status", EntityStatus.INACTIVE)

    def update(self, employee_id: int, field: str, value: Any) -> Employee:
        employee: Employee = self.get_employee(employee_id)

        if not hasattr(employee, field):
            raise ValueError("This field doesn't exist")

        setattr(employee, field, value)
        employee.updated_at = datetime.now()

        return employee

    def list_employees(
        self,
        key: Callable[[Employee], Any] = lambda employee: employee.id,
        reverse: bool = False,
    ) -> list[Employee]:
        filtered_employees = [employee for employee in self._db.values() if employee.status == EntityStatus.ACTIVE]
        return sorted(filtered_employees, key=key, reverse=reverse)

    def _generate_next_id(self):
        self._current_id += 1

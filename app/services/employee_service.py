from app.domains.employee import Employee


class EmployeeService:
    def __init__(self) -> None:
        self._employee_list = dict[int, Employee] = {}
        self._current_id = 1

    def create(
        self,
        status,
        created_by,
        created_at,
        first_name,
        last_name,
        address,
        email,
        phone,
        role,
    ) -> Employee:
        employee = Employee(
            id=self._current_id,
            status=status,
            created_by=created_by,
            updated_by=created_by,
            created_at=created_at,
            updated_at=created_at,
            first_name=first_name,
            last_name=last_name,
            address=address,
            email=email,
            phone=phone,
            role=role,
        )

        self._employee_list[self._current_id] = employee
        self._current_id = self._current_id + 1

        return employee

    def get_employee(self) -> Employee:
        return self._employee_list.get(id)

    def update_employee(
        self,
        status,
        updated_by,
        updated_at,
        first_name,
        last_name,
        address,
        email,
        phone,
        role,
    ) -> Employee:
        current_employee = self._employee_list.get(id)

        current_employee.status = status
        current_employee.updated_by = updated_by
        current_employee.updated_at = updated_at
        current_employee.first_name = first_name
        current_employee.last_name = last_name
        current_employee.address = address
        current_employee.email = email
        current_employee.phone = phone
        current_employee.role = role

        return current_employee

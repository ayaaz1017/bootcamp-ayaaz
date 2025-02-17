from typing import Dict

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: Dict[int, Employee] = {}  # Key: emp_id, Value: Employee object

    def add_employee(self, employee: Employee) -> None:
        self.employees[employee.emp_id] = employee  # Store by emp_id for quick lookup

    def get_employee(self, emp_id: int) -> Employee:
        return self.employees.get(emp_id, None)

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {list(self.employees.values())}"

# Example Usage
dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

print(dept.get_employee(101))  # Alice (Developer)


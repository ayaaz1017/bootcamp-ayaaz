class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: Dict[int, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id: int) -> None:
        if emp_id in self.employees:
            del self.employees[emp_id]

    def calculate_total_salary(self) -> float:
        return sum(emp.salary for emp in self.employees.values())

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {list(self.employees.values())}"

# Example Usage
print(f"Total Department Salary: {dept.calculate_total_salary()}")  # 140000
dept.remove_employee(102)
print(dept)  # Bob removed

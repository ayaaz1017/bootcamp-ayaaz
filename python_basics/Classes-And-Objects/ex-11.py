from typing import List

class Employee:
    def __init__(self, name: str, emp_id: int, position: str, salary: float) -> None:
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} ({self.position})"

class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def __str__(self) -> str:
        return f"Department: {self.name}, Employees: {[str(emp) for emp in self.employees]}"


emp1 = Employee("Alice", 101, "Developer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)

dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

print(dept)

from typing import List

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def __str__(self) -> str:
        return f"Project: {self.name}, Employees: {[emp.name for emp in self.employees]}"

project = Project("Cloud Migration", dept)
project.add_employee(emp1)
print(project)

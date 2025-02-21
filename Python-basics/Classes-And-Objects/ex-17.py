from typing import List

class Project:
    def __init__(self, name: str, department: Department) -> None:
        self.name = name
        self.department = department  
        self.employees: List[Employee] = []  

    def add_employee(self, employee: Employee) -> None:
        """Assigns an employee to the project"""
        self.employees.append(employee)

    def remove_employee(self, emp_id: int) -> None:
        """Removes an employee from the project by ID"""
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self) -> List[str]:
        """Returns a list of employee names in the project"""
        return [emp.name for emp in self.employees]

    def __str__(self) -> str:
        return f"Project: {self.name}, Department: {self.department.name}, Employees: {self.list_employees()}"

# Example Usage
dept = Department("IT")  

# Create Employees
emp1 = Employee("Alice", 101, "Developer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)

# Add employees to the department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Create a project under the IT department
project = Project("Cloud Migration", dept)

# Assign employees to the project
project.add_employee(emp1)
project.add_employee(emp2)

# Display project details
print(project)  

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        employee.department = self  
        self.employees.append(employee)

    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.name} works as {employee.position} in {self.name}")


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.department = None  
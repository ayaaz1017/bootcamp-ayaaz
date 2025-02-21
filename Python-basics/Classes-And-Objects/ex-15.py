class Employee:
    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary}, position={self.position})"

class Manager(Employee):
    def __repr__(self):
        return f"Manager(name={self.name}, salary={self.salary}, position={self.position}, subordinates={len(self.subordinates)})"

class Department:
    def __repr__(self):
        return f"Department(name={self.name}, employees={len(self.employees)})"

class Project:
    def __repr__(self):
        return f"Project(name={self.name}, department={self.department.name}, employees={len(self.employees)})"

# Test
print(repr(emp1))
print(repr(manager))
print(repr(dept))
print(repr(project))
class Employee:
    def __init__(self, name, emp_id, position): # type: ignore
        self.name = name
        self.emp_id = emp_id
        self.position = position
        
emp1 = Employee("Bunny",1,"Developer")

print(emp1.__dict__)



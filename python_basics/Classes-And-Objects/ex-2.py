class Employee:
    def __init__(self, name: str, emp_id: int, position: str):
        self.name: str = name
        self.emp_id: int = emp_id
        self.position: str = position
        
emp1 = Employee("Bunny",1,"Developer")

print(emp1.__dict__)



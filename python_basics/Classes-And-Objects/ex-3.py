

class Employee:
    def __init__(self, name: str, emp_id: int, position: str) -> None:
        self.name: str = name
        self.emp_id: int = emp_id
        self.position: str = position


e1 = Employee("Ashkok", 101, "Developer")
e2 = Employee("Naresh", 102, "Tester")
print(e1.__dict__)
print(e2.__dict__)

class Employee:
    def __str__(self) -> str:
        return f"{self.name} ({self.position})"

    def __repr__(self) -> str:
        return f"Employee(name='{self.name}', emp_id={self.emp_id}, position='{self.position}')"

print(repr(emp1))  

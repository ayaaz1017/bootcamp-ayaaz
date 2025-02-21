class Employee:
    def __init__(self, name: str, emp_id: int, position: str, salary: float) -> None:
        self.name = name
        self.emp_id = emp_id
        self._position = position 
        self._salary = salary

    @property
    def position(self) -> str:
        """Getter for position"""
        return self._position

    @position.setter
    def position(self, new_position: str) -> None:
        """Setter with validation"""
        if not new_position:
            raise ValueError("Position cannot be empty!")
        self._position = new_position

    @property
    def salary(self) -> float:
        """Getter for salary"""
        return self._salary

    @salary.setter
    def salary(self, new_salary: float) -> None:
        """Setter with validation"""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = new_salary

    def __str__(self) -> str:
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self.position}, Salary: ${self.salary}"

# Example Usage
emp = Employee("Alice", 101, "Developer", 60000)
print(emp)  

# Updating position (Valid)
emp.position = "Senior Developer"
print(emp.position) 

# Updating salary (Valid)
emp.salary = 70000
print(emp.salary) 
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

class Manager(Employee):
    def __init__(self, name, salary, position):
        super().__init__(name, salary, position)
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def __str__(self):
        return f"{super().__str__()} manages {len(self.subordinates)} employees"


manager = Manager("Alice", 80000, "Senior Manager")
emp1 = Employee("Bob", 50000, "Developer")
emp2 = Employee("Charlie", 60000, "Designer")
manager.add_subordinate(emp1)
manager.add_subordinate(emp2)
print(manager)



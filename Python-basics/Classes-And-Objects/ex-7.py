class Manager:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def manage(self):
        print(f"{self.name} is managing the team.")
        
        
solution = Manager("Bunny",22,100000)

print(solution.__dict__)
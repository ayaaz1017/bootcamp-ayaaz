

class SuperManager(Manager):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def manage_subordinates(self):
        for subordinate in self.subordinates:
            print(f"{self.name} is managing {subordinate.name}")
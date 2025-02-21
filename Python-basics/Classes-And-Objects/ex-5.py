class Employee:
    def __init__(self,name: str, emp_id: int, position: str):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        
    def update_position(self,new_position: str) -> None:
        self.position = new_position
        
    def display_info(self) -> str:
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self.position}"




    
e1 = Employee("Bunny",777,"DevOps")

print(e1.__dict__)


e1.update_position("backend dev")

print(e1.display_info())
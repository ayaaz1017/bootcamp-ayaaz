class Employee:
    def __init__(self,name: str, emp_id: int, position: str):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        
    def update_name(self,new_name: str) -> None:
        self.position = new_name
        
    def update_emp_id(self,new_id: str) -> None:
        self.emp_id = new_id
        
    def update_position(self,new_position: str) -> None:
        self.position = new_position
        
    def display_info(self) -> str:
        return f"Employee: {self.name}, ID: {self.emp_id}, Position: {self.position}"





e1 = Employee("Bunny",777,"DevOps")

print(e1.__dict__)


e1.update_position("backend dev")
e1.update_emp_id('888')
e1.update_name("Srinivas")

print(e1.display_info())
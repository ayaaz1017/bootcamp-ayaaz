from typing import List

class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: List[Department] = []
        self.projects: List[Project] = []

    def add_department(self, department: Department) -> None:
        """Adds a new department to the company"""
        self.departments.append(department)

    def add_project(self, project: Project) -> None:
        """Adds a new project to the company"""
        self.projects.append(project)

    def assign_employee_to_project(self, emp: Employee, project_name: str) -> None:
        """Assigns an employee to a project by name"""
        for project in self.projects:
            if project.name == project_name:
                project.add_employee(emp)
                return
        raise ValueError(f"Project '{project_name}' not found!")

    def department_summary(self) -> None:
        """Prints a summary of all departments and their employees"""
        print(f"\nCompany: {self.name} - Departments Summary")
        for dept in self.departments:
            print(f"\nDepartment: {dept.name}, Employees: {dept.list_employees()}")

    def project_summary(self) -> None:
        """Prints a summary of all projects and their assigned employees"""
        print(f"\nCompany: {self.name} - Projects Summary")
        for proj in self.projects:
            print(f"\n{proj}")

# Example Usage
company = Company("TechCorp")

# Create Departments
it_department = Department("IT")
hr_department = Department("HR")
company.add_department(it_department)
company.add_department(hr_department)

# Create Employees
emp1 = Employee("Alice", 101, "Developer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)
emp3 = Employee("Charlie", 103, "HR Lead", 75000)

# Add Employees to Departments
it_department.add_employee(emp1)
it_department.add_employee(emp2)
hr_department.add_employee(emp3)

# Create Projects
project1 = Project("Cloud Migration", it_department)
project2 = Project("HR System Upgrade", hr_department)
company.add_project(project1)
company.add_project(project2)

# Assign Employees to Projects
company.assign_employee_to_project(emp1, "Cloud Migration")
company.assign_employee_to_project(emp2, "Cloud Migration")
company.assign_employee_to_project(emp3, "HR System Upgrade")

# Print Summaries
company.department_summary()
company.project_summary()

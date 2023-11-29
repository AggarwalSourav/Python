AIM: WRITE A PROGRAM TO IMPLEMENT AN EMPLOYEE MANAGEMENT SYSTEM USING CLASSES, INSTANCES, AND INHERITANCE.
# Parent class Employee
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

# Child class Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):  # Overriding the display_info method
        super().display_info()
        print(f"Department: {self.department}")

# Creating instances of Employee and Manager classes
employee1 = Employee(1001, "John Doe", 50000)
manager1 = Manager(2001, "Alice Smith", 70000, "HR")

# Displaying employee and manager information
print("Employee Information:")
employee1.display_info()
print("\nManager Information:")
manager1.display_info()

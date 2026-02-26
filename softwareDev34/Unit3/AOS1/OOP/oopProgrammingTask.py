class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
    
class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)
            self.bonus = bonus
        
        def display_details(self):
            super().display_details()
            print(f"Manager Bonus: {self.bonus}")

employee1 = Employee("Alice", 50000)
employee1.display_details()
print("\n")
manager1 = Manager("Bob", 80000, 10000)
manager1.display_details()

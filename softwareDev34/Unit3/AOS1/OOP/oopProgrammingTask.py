class Employee:
    """
    Base class for all employees.
    
    IPO:
        Input: name (str), salary (int/float)
        Processing: Stores employee data as instance attributes
        Output: Displays formatted employee details via display_details()
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")

class Manager(Employee):
    """
    Manager class that extends Employee with bonus information.
    
    IPO:
        Input: name (str), salary (int/float), bonus (int/float)
        Processing: Inherits Employee attributes, adds bonus attribute
        Output: Displays employee details plus manager bonus
    """
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def display_details(self):
        super().display_details()
        print(f"Manager Bonus: {self.bonus}")


# --- Main Program Execution ---
# Input: Hardcoded employee and manager data
# Processing: Create Employee and Manager objects
# Output: Display details for each

employee1 = Employee("Alice", 50000)
employee1.display_details()
print("\n")
manager1 = Manager("Bob", 80000, 10000)
manager1.display_details()

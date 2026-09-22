# ============================================
# PARENT CLASS
# ============================================
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name       : {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary     : ₹{self.salary}")

    def work(self):
        print(f"{self.name} is working.")


# ============================================
# CHILD 1 — Developer
# ============================================
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language, project):
        super().__init__(name, employee_id, salary)     # parent's __init__
        self.programming_language = programming_language
        self.project = project

    def work(self):                                     # override
        print(f"{self.name} is developing the {self.project} using {self.programming_language}")


# ============================================
# CHILD 2 — Tester
# ============================================
class Tester(Employee):
    def __init__(self, name, employee_id, salary, testing_tool, project):
        super().__init__(name, employee_id, salary)
        self.testing_tool = testing_tool
        self.project = project

    def work(self):                                     # override
        print(f"{self.name} is testing the {self.project} using {self.testing_tool}")


# ============================================
# CHILD 3 — HR
# ============================================
class HR(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def work(self):                                     # override
        print(f"{self.name} is managing the {self.department} department")


# ============================================
# CREATE OBJECTS
# ============================================
dev     = Developer("Arun",  "E101", 60000, "Python",   "Employee Portal")
tester  = Tester   ("Priya", "E102", 45000, "Selenium", "Employee Portal")
hr      = HR       ("Meena", "E103", 40000, "HR")

# ============================================
# DISPLAY DETAILS + CALL work()
# ============================================
for emp in [dev, tester, hr]:
    print("=" * 40)
    emp.display_details()      # inherited from Employee
    emp.work()                 # overridden in each child
    print()
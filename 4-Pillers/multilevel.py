# ---------- Parent 1 ----------
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Name       : {self.name}")
        print(f"Employee ID: {self.employee_id}")


# ---------- Parent 2 ----------
class Skills:
    def __init__(self, skill):
        self.skill = skill

    def display_skill(self):
        print(f"Skill      : {self.skill}")


# ---------- Child ----------
class Developer(Employee, Skills):
    def __init__(self, name, employee_id, skill, project):
        Employee.__init__(self, name, employee_id)   # parent 1
        Skills.__init__(self, skill)                 # parent 2
        self.project = project

    def work(self):
        print(f"{self.name} is working on {self.project}.")


# ---------- Create Object ----------
dev = Developer("Priya", "E101", "Python", "Chat App")

print("===== DEVELOPER INFO =====")
dev.display_employee()     # from Employee
dev.display_skill()        # from Skills
print(f"Project    : {dev.project}")
dev.work()                 # own method
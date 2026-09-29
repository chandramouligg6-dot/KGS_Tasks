class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Name       : {self.name}")
        print(f"Employee ID: {self.employee_id}")

class Skills:
    def __init__(self, skill):
        self.skill = skill

    def display_skill(self):
        print(f"Skill      : {self.skill}")

class Developer(Employee, Skills):
    def __init__(self, name, employee_id, skill, project):
        Employee.__init__(self, name, employee_id)
        Skills.__init__(self, skill)
        self.project = project

    def work(self):
        print(f"{self.name} is working on {self.project}.")

dev = Developer("Priya", "E101", "Python", "Chat App")

print("===== DEVELOPER INFO =====")
dev.display_employee()
dev.display_skill()
print(f"Project    : {dev.project}")
dev.work()
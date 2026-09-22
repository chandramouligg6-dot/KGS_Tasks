# ---------- Parent Class ----------
class Employee:
    def work(self):
        print("Employee is working")


# ---------- Child 1 ----------
class Developer(Employee):
    def work(self):
        print("Developer → Writing code")


# ---------- Child 2 ----------
class Tester(Employee):
    def work(self):
        print("Tester → Testing application")


# ---------- Child 3 ----------
class Manager(Employee):
    def work(self):
        print("Manager → Managing team")


# ---------- Create Objects ----------
dev = Developer()
tester = Tester()
manager = Manager()

dev.work()
tester.work()
manager.work()
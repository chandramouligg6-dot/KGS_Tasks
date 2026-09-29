class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer → Writing code")

class Tester(Employee):
    def work(self):
        print("Tester → Testing application")

class Manager(Employee):
    def work(self):
        print("Manager → Managing team")

dev = Developer()
tester = Tester()
manager = Manager()

dev.work()
tester.work()
manager.work()
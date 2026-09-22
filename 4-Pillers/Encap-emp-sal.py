class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            print("Invalid salary.")
        else:
            self.__salary = new_salary


e = Employee("Priya", 30000)

e.set_salary(35000)
print(e.get_salary())

e.set_salary(-5000)
print(e.get_salary())
# # Parent class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person(self):
#         print(f"Name: {self.name}")
#         print(f"Age : {self.age}")


# # Child class
# class Student(Person):
#     def __init__(self, name, age, student_id, course):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.course = course

#     def display_student(self):
#         self.display_person()
#         print(f"Student ID: {self.student_id}")
#         print(f"Course    : {self.course}")


# s = Student("Priya", 20, "S101", "Computer Science")
# s.display_student()























# Dynamic code to take input from user and display studen information.


# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")


# Child class
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Student ID: {self.student_id}")
        print(f"Course    : {self.course}")


print("Enter Student Details")
print("-" * 25)

name = input("Enter name       : ")
age = int(input("Enter age        : "))
student_id = input("Enter student ID : ")
course = input("Enter course     : ")

s = Student(name, age, student_id, course)

print("\n--- Student Information ---")
s.display_student()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def diagnose(self):
        print(f"Dr. {self.name} ({self.specialization}) is diagnosing.")


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def treatment(self):
        print(f"{self.name} of an age {self.age} is receiving treatment for {self.disease}.")


print("===== DOCTOR =====")
d = Doctor("Meera", 45, "Cardiology")
d.display_info()
print(f"Specialization: {d.specialization}")
d.diagnose()

print("\n===== PATIENT =====")
p = Patient("Arjun", 30, "Fever")
p.display_info()
print(f"Disease: {p.disease}")
p.treatment()
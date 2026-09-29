from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass

class Pizza(Food):
    def prepare(self):
        print("Pizza → Preparing pizza")

    def serve(self):
        print("Pizza → Serving pizza")

class Burger(Food):
    def prepare(self):
        print("Burger → Preparing burger")

    def serve(self):
        print("Burger → Serving burger")

class Biryani(Food):
    def prepare(self):
        print("Biryani → Preparing biryani")

    def serve(self):
        print("Biryani → Serving biryani")

for food in [Pizza(), Burger(), Biryani()]:
    food.prepare()
    food.serve()
    print("-" * 30)
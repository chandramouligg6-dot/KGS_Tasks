from abc import ABC, abstractmethod

# ---------- Abstract Parent ----------
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass


# ---------- Child 1 ----------
class Pizza(Food):
    def prepare(self):
        print("Pizza → Preparing pizza")

    def serve(self):
        print("Pizza → Serving pizza")


# ---------- Child 2 ----------
class Burger(Food):
    def prepare(self):
        print("Burger → Preparing burger")

    def serve(self):
        print("Burger → Serving burger")


# ---------- Child 3 ----------
class Biryani(Food):
    def prepare(self):
        print("Biryani → Preparing biryani")

    def serve(self):
        print("Biryani → Serving biryani")


# ---------- Test ----------
for food in [Pizza(), Burger(), Biryani()]:
    food.prepare()
    food.serve()
    print("-" * 30)
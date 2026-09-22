# ---------- Class 1 ----------
class Pizza:
    def prepare(self):
        print("Pizza → Preparing pizza")


# ---------- Class 2 ----------
class Burger:
    def prepare(self):
        print("Burger → Preparing burger")


# ---------- Class 3 ----------
class Biryani:
    def prepare(self):
        print("Biryani → Preparing biryani")


# ---------- Polymorphic function ----------
def order_food(food):
    food.prepare()


# ---------- Test with all three objects ----------
order_food(Pizza())
order_food(Burger())
order_food(Biryani())
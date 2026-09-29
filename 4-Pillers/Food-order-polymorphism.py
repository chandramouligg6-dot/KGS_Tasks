
class Pizza:
    def prepare(self):
        print("Pizza → Preparing pizza")

class Burger:
    def prepare(self):
        print("Burger → Preparing burger")

class Biryani:
    def prepare(self):
        print("Biryani → Preparing biryani")

def order_food(food):
    food.prepare()

order_food(Pizza())
order_food(Burger())
order_food(Biryani())
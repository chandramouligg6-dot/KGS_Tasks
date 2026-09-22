# ---------- Parent Class ----------
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price       : ₹{self.price}")


# ---------- Child 1 ----------
class Electronics(Product):
    def __init__(self, product_name, price, warranty):
        super().__init__(product_name, price)
        self.warranty = warranty

    def display_warranty(self):
        print(f"Warranty    : {self.warranty} years")


# ---------- Child 2 ----------
class Clothing(Product):
    def __init__(self, product_name, price, size):
        super().__init__(product_name, price)
        self.size = size

    def display_size(self):
        print(f"Size        : {self.size}")


# ---------- Create Objects ----------
print("===== ELECTRONICS =====")
e = Electronics("Laptop", 55000, 2)
e.display_product()
e.display_warranty()

print("\n===== CLOTHING =====")
c = Clothing("T-Shirt", 799, "M")
c.display_product()
c.display_size()
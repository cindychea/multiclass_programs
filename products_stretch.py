class Product:
    def __init__(self, name, base_price, quantity=1):
        self.name = name
        self.base_price = base_price
        self.quantity = quantity

    def __str__(self):
        return "{}".format(self.name)
    
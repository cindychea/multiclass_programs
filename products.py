class Product:
    def __init__(self, name, base_price, tax_rate, quantity=1):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate
        self.quantity = quantity

    def __str__(self):
        return "{}".format(self.name)
    
    def total_price(self):
        total_price = (self.base_price * self.tax_rate + self.base_price) * self.quantity
        return total_price


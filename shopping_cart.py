from products import Product

class ShoppingCart:
    def __init__(self):
        self.products = []

    def __str__(self):
        return "Your shopping cart has the following items:\n" + '\n'.join(str(product) for product in self.products)
    
    def add_item(self, product):
        self.products.append(product)
        return "You added {} to your cart.".format(product.name)

    def rem_item(self, product):
        self.products.remove(product)
        return "You removed {} from your cart.".format(product.name)

    def subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product.base_price * product.quantity
        return "Your total before tax is ${}.".format(subtotal)

    def total(self):
        total = 0
        for product in self.products:
            total += product.total_price()
        return "Your total after tax is ${}.".format(total)

    def most_expensive(self):
        prices = []
        for product in self.products:
            prices.append(product.base_price)
        expensive_item = max(prices)
        return "The most expensive item is {} at ${}".format(product.name, expensive_item)

train = Product('Thomas the Tank Engine', 15, 0.13)
car = Product('Lightning McQueen', 25, 0.13)
bus = Product('The Magic School Bus', 20, 0.13)
shopping_cart = ShoppingCart()

shopping_cart.add_item(train)
shopping_cart.add_item(car)
shopping_cart.add_item(bus)
shopping_cart.add_item(car)
shopping_cart.add_item(car)

shopping_cart.rem_item(car)

print(shopping_cart)
print(shopping_cart.subtotal())
print(shopping_cart.total())
print(shopping_cart.most_expensive())

# STRETCH GOALS
# Add the ability to find the most expensive product in a cart.
# Allow a quantity to be associated with each product in the cart. What is the best way to store this information? How does it affect each of your other methods?
# Instead of storing the tax rate for each product, come up with a tax classification system (eg. standard, tax exempt, imported) so the rates are standardized across all products.
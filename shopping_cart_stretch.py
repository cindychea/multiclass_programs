from products import Product

class ShoppingCart:

    def __init__(self):
        self.products = []
        self.cart_items = {}

    def __str__(self):
        return "Your shopping cart has the following items:\n" + '\n'.join(str(product) for product in self.products)
    
    def add_item(self, product):
        self.products.append(product)
        for item in self.cart_items.items():
            if item == product:
                self.cart_items[product] += 1
            else: 
                self.cart_items[product] = 1
        return "You added {} to your cart.".format(product.name)

    def rem_item(self, product):
        self.products.remove(product)
        return "You removed {} from your cart.".format(product.name)

    def subtotal(self):
        subtotal = 0
        for product in self.products:
            subtotal += product.base_price * product.quantity
        return subtotal

    def total(self):
        total_price = 0
        print("Please enter the tax rate: Standard (13%), Exempt (No Tax), or Imported (20%).")
        tax = input()
        for product in self.products:
            if tax == 'standard' or tax == 'Standard':
                total_price += product.base_price * product.quantity * 1.13
            elif tax == 'exempt' or tax == 'Exempt':
                total_price += product.base_price * product.quantity
            elif tax == 'imported' or tax == 'Imported':
                total_price += product.base_price * product.quantity * 1.20
            else:
                print("Invalid tax rate")
        return "Your total after tax is ${}.".format(total_price)

    def most_expensive(self):
        prices = []
        for product in self.products:
            prices.append(product.base_price)
        expensive_item = max(prices)
        return "The most expensive item is {} at ${}".format(product.name, expensive_item)

train = Product('Thomas the Tank Engine', 15)
car = Product('Lightning McQueen', 25)
bus = Product('The Magic School Bus', 20)
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
# print(ShoppingCart.cart_items)

# STRETCH GOALS
# Add the ability to find the most expensive product in a cart.
# Allow a quantity to be associated with each product in the cart. What is the best way to store this information? How does it affect each of your other methods?
# Instead of storing the tax rate for each product, come up with a tax classification system (eg. standard, tax exempt, imported) so the rates are standardized across all products.
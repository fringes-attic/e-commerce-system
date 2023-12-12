# order.py

class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products

    def display_info(self):
        print(f"Order ID: {self.order_id}")
        self.customer.display_info()
        print("Products:")
        for product in self.products:
            product.display_info()

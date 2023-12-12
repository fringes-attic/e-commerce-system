# ecommerce_system.py

from customer import Customer
from product import Product
from order import Order

# Create customers
customer1 = Customer(1, "Alice", "alice@example.com")
customer2 = Customer(2, "Bob", "bob@example.com")

# Create products
product1 = Product(101, "Laptop", 999.99)
product2 = Product(102, "Smartphone", 599.99)

# Create orders
order1 = Order(1, customer1, [product1, product2])
order2 = Order(2, customer2, [product2])

# Display order information
print("Order Information:")
order1.display_info()
print()
order2.display_info()

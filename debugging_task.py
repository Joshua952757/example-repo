def calculate_total(a, b):
    """Returns the product of two numbers."""
    return a * b

def get_item_price(item, prices):
    """Returns the price of an item or 'Not Found' if missing."""
    return prices.get(item, "Not Found")

def divide_numbers(x, y):
    """Divides two numbers, returns 'Undefined' if divided by zero."""
    return x / y if y != 0 else "Undefined"

# Sample data
prices = {"apple": 1.2, "banana": 0.5, "orange": 0.8}

# Test cases
print(calculate_total(2, 3))
print(get_item_price("grape", prices))
print(divide_numbers(10, 0))

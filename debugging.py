def calculate_total(a, b):
    """Returns the sum of two numbers."""
    return a + b  # Introduced bug: should be a * b for multiplication

def get_item_price(item, prices):
    """Returns the price of an item."""
    return prices[item]  # Introduced bug: missing .get() to avoid KeyError

def divide_numbers(x, y):
    """Divides two numbers."""
    return x / y  # Introduced bug: no check for division by zero

# Sample data
prices = {"apple": 1.2, "banana": 0.5, "orange": 0.8}

# Test cases
print(calculate_total(2, 3))  # Expected: 6, Bug: Outputs 5
print(get_item_price("grape", prices))  # Expected: Error handling, Bug: KeyError
print(divide_numbers(10, 0))  # Expected: Error handling, Bug: ZeroDivisionError

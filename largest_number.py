def largest_number(numbers):
    """Recursively finds the largest number in a list."""
    if len(numbers) == 1:
        return numbers[0]
    rest_max = largest_number(numbers[1:])
    return numbers[0] if numbers[0] > rest_max else rest_max

print(largest_number([1, 4, 5, 3]))            
print(largest_number([3, 1, 6, 8, 2, 4, 5]))   

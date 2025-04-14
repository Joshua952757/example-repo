import statistics

def get_numbers():
    return [float(input(f"Enter number {i+1}: ")) for i in range(10)]

def calculate_statistics(numbers):
    total = sum(numbers)
    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))
    average = round(statistics.mean(numbers), 2)
    median = statistics.median(numbers)
    
    print(f"Total: {total}")
    print(f"Index of Maximum: {max_index}")
    print(f"Index of Minimum: {min_index}")
    print(f"Average: {average}")
    print(f"Median: {median}")

numbers = get_numbers()
calculate_statistics(numbers)

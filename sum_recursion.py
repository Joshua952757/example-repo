def adding_up_to(numbers, index):

    if index == 0:
        return numbers[0]
    return numbers[index] + adding_up_to(numbers, index - 1)

print("\nCalculating recursive sum function:")
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  
print(adding_up_to([4, 3, 1, 5], 1))      
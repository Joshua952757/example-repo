numbers_list = input("Please enter 3 different integers (seperated by spaces):\n")
numbers_list = numbers_list.split()
numbers_list = [int(num)for num in numbers_list]

print(sum(numbers_list))

if len(numbers_list) >=2:
     print(numbers_list[0]-numbers_list[1])
else:
    print("Not enough numbers on the number_list!")
    
if len(numbers_list) >=2:
    print(numbers_list[2]*[0])
else:
    print("Not enough numbers on the numbers_list!")
    
sum_of_numbers = sum(numbers_list)
result = numbers_list[2]/sum_of_numbers

print(result)
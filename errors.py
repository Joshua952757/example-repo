# Code (with errors)
# print("Hello, world"

# Fixing: Added the missing closing bracket. (Syntax Error)
print("Hello, world")  

# x = 10
# y = "5"
# print(x + y)

# Fixing: Can't add a number and a string. Convert y to an integer.(Runtime Error)
x = 10
y = "5"
print(x + int(y))  

# def say_hello
#     print("Hello!")

# Fixing: Added missing bracket after function name. (Syntax Error)
def say_hello():
    print("Hello!")

say_hello()

# Original Code (with errors)
# numbers = [1, 2, 3]
# print(numbers[5])

# Fixing: Index 5 is out of range. Use a valid index.(Runtime Error)
numbers = [1, 2, 3]
# Fixed by using a valid index
print(numbers[2])  

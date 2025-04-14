# Code (with errors)
# name = input("Enter your name: ")
# print("Hello" + name)

# Fixing: Added space after "Hello" so the output looks correct. (Logical Error)
name = input("Enter your name: ")
print("Hello " + name)  

# for i in range(5)
#     print(i)

# Fixing: Added missing colon at the end of the loop. (Syntax Error)
for i in range(5):
    print(i)

# age = input("Enter your age: ")
# if age > 18:
#     print("You are an adult.")

# Fixing: Convert age to an integer before comparing. (Runtime Error)
age = int(input("Enter your age: "))  
if age > 18:
    print("You are an adult.")

# def add_numbers(a, b):
# return a + b

# Fixing: Indented the return statement correctly. (Syntax Error)
def add_numbers(a, b):
    return a + b  

result = add_numbers(3, 4)
print(result)  

import os

def save_equation(equation):
    with open("equations.txt", "a") as file:
        file.write(equation + "\n")

def load_equations():
    if not os.path.exists("equations.txt"):
        print("No previous calculations found.")
        return
    with open("equations.txt", "r") as file:
        print("Previous calculations:")
        print(file.read())

def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        equation = f"{num1} {operator} {num2} = {result}"
        print("Result:", equation)
        save_equation(equation)
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")

def main():
    while True:
        choice = input("Choose an option: (1) Calculate (2) View history (3) Exit: ")
        if choice == '1':
            calculate()
        elif choice == '2':
            load_equations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

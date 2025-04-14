valid_numbers = []
while True:
    valid_number = input("Please enter a number (-1 to stop):\n")
    try:
        valid_number = int(valid_number)
        if valid_number == -1:
            print("Stopping program.")
            break
        elif valid_number == 0:
            print("Zero is not a valid input. Please try again.")
        else:
            valid_numbers.append(valid_number)
            print("You entered:", valid_number)
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if valid_numbers:
    average = sum(valid_numbers) / len(valid_numbers)
    print("Average of valid numbers:", average)
else:
    print("No valid numbers entered.")


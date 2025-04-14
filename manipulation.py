str_manip = input("Please enter a sentence.")
size = len(str_manip)

print(size)

replaced = str_manip.replace("e","@")

print(replaced)

size = len(str_manip)

print(size)
print(str_manip[-3:size])

first_three = str_manip[:4]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two

print("The five letter word is:",five_letter_word)
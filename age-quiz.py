age = int(input("Please enter your age:\n"))

if age < 13:
    print("You qualify for the kiddies discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 40:
    print("You're over the hill.")
elif age > 65:
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry,you're dead.")
else:
    print("Age is but a number.")
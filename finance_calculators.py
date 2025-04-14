import math

print("Choose the finance calculation you would like to see:")
print("Investment: See the interest on your savings")
print("Bond: See your home loan repayment")

user_choice = input("Enter 'Investment' or 'Bond': \n").lower()

if user_choice == "investment":
    p = float(input("Deposit amount: "))
    r = float(input("Interest rate(%): ")) / 100
    t = int(input("Years: "))
    
    interest = input("Simple or compound interest?: ").lower()
    
    if interest == "simple":
        A = p * (1 + (r * t))
    elif interest == "compound":
        A = p * (1 + r) ** t
    else:
        print("Your interest type is invalid")
        exit()
        
    print("Your total amount after", t, "years:", round(A, 2))
    
elif user_choice == "bond":
    p = float(input("The House value: "))
    r = float(input("Interest rate: ")) / 100 / 12
    n = int(input("Number of months to repay: "))
    
    repayment = round(float((r * p) / (1 - (1 + r) ** -n)), 2)

    print("Monthly repayment:" , repayment)
    
else:
    print("Your choice is invalid. Please enter either 'investment' or 'bond'.")
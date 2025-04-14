"""
Shoe Inventory Manager
Reads shoe data, lets users manage and update inventory.
"""

class Shoe:
    """Represents a Shoe with basic details."""
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Returns cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Returns quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """String representation of the shoe."""
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# List to store shoe objects
shoes_list = []

# Function to read data from file
def read_shoes_data():
    """Reads shoe data from inventory.txt and creates shoe objects."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)  
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
    except FileNotFoundError:
        print("File not found. Make sure inventory.txt exists.")

def capture_shoes():
    """Captures new shoe info from user and adds to list."""
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe added.\n")

# Function to view all shoes
def view_all():
    """Prints all shoes in inventory."""
    for shoe in shoes_list:
        print(shoe)

# Function to restock lowest quantity shoe
def re_stock():
    """Finds shoe with lowest quantity and offers to restock it."""
    if not shoes_list:
        print("No shoes to restock.")
        return
    lowest = min(shoes_list, key=lambda s: s.get_quantity())
    print("Lowest stock:", lowest)
    add_qty = input("Add quantity to this item? (yes/no): ").lower()
    if add_qty == "yes":
        amount = int(input("How many to add?: "))
        lowest.quantity += amount
        
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(f"{shoe}\n")
        print("Stock updated.")

# Function to search shoe by code
def search_shoe():
    """Searches for a shoe by code."""
    code = input("Enter shoe code: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print("Shoe found:", shoe)
            return
    print("Shoe not found.")

# Function to show total value of each item
def value_per_item():
    """Shows value (cost * quantity) of each shoe."""
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: R{value}")

# Function to show item with highest quantity
def highest_qty():
    """Finds and prints the shoe with the highest quantity."""
    if not shoes_list:
        print("No shoes in stock.")
        return
    highest = max(shoes_list, key=lambda s: s.get_quantity())
    print("*** FOR SALE ***")
    print(highest)

# MAIN MENU
read_shoes_data() 

while True:
    print("\n--- Shoe Inventory Menu ---")
    print("1. View all shoes")
    print("2. Add new shoe")
    print("3. Restock low quantity")
    print("4. Search shoe by code")
    print("5. Show value per item")
    print("6. Show item for sale")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_all()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

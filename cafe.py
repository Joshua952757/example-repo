def main():
    """Calculate total stock value in the café."""
    menu = ["Coffee", "Tea", "Sandwich", "Cake"]
    
    stock = {"Coffee": 20, "Tea": 30, "Sandwich": 15, "Cake": 10}
    price = {"Coffee": 3.00, "Tea": 2.50, "Sandwich": 5.00, "Cake": 4.00}
    
    total_stock = sum(stock[item] * price[item] for item in menu)
    
    print(f"Total stock value: ${total_stock:.2f}")

if __name__ == "__main__":
    main()
def main():
    """Stores incorrect names until 'John' is entered."""
    incorrect_names = []
    
    while True:
        name = input("Enter your name: ")
        if name == "John":
            break
        incorrect_names.append(name)
    
    print("\nIncorrect names:", incorrect_names)
    """Runs the program
    """
if __name__ == "__main__":
    main()

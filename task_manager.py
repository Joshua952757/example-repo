import datetime

# Store users in a dictionary
users = {}

# Load existing users from file
with open('user.txt', 'r') as f:
    # Reads and loads usernames and passwords
    for line in f:
        parts = line.strip().split(', ')
        if len(parts) == 2:
            username, password = parts
            users[username] = password
        else:
            print(f"Skipping invalid line in user.txt: {line}")

# User login loop
while True:
    """Log in the user by checking credentials."""
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users and users[username] == password:
        print("You have successfully logged in.\n")
        break
    else:
        print("Login failed. Please try again.\n")

# Main menu loop
while True:
    """Show menu and handle user's selection."""
    menu = input('''Select one of the following options:
r  - register a user                
a  - add task               
va - view all tasks                
vm - view my tasks                 
e  - exit                
: ''').lower().strip()
    
    if menu == 'r':
        """Register a new user."""
        new_user = input("Enter new username: ").strip()
        if new_user in users:
            print("This username already exists.\n")
            continue
        new_pass = input("Enter new password: ").strip()
        conf_pass = input("Confirm the new password: ").strip()
        if new_pass == conf_pass:
            with open('user.txt', 'a') as f:
                f.write(f"\n{new_user}, {new_pass}")
            users[new_user] = new_pass
            print("User registered.\n")
        else:
            print("Passwords do not match.\n")

    elif menu == 'a':
        """Add a new task and assign it to a user."""
        task_user = input("Enter username to assign task to: ").strip()
        if task_user not in users:
            print("That user does not exist.\n")
            continue
        title = input("Enter task title: ").strip()
        desc = input("Enter task description: ").strip()
        due = input("Enter due date (e.g. 25 April 2025): ").strip()
        today = datetime.date.today().strftime("%d %b %Y")
        completed = "No"

        with open('tasks.txt', 'a') as f:
            f.write(f"\n{task_user}, {title}, {desc}, {due}, {today}, {completed}")
        
        print("Task added.\n")

    elif menu == 'va':
        """View all tasks in the system."""
        print("\nAll Tasks\n")
        with open('tasks.txt', 'r') as f:
            for line in f:
                task = line.strip().split(', ')
                if len(task) == 6:
                    print(f'''
Task:        {task[1]}
Assigned to: {task[0]}
Date assigned: {task[4]}
Due date:   {task[3]}
Task complete? {task[5]}
Description: {task[2]}
''')
                else:
                    print(f"Skipping malformed task line: {line}")

    elif menu == 'vm':
        """View tasks assigned to the current user."""
        print("\nMy Tasks\n")
        with open('tasks.txt', 'r') as f:
            for line in f:
                task = line.strip().split(', ')
                if len(task) == 6 and task[0] == username:
                    print(f'''
Task:        {task[1]}
Assigned to: {task[0]}
Date assigned: {task[4]}
Due date:   {task[3]}
Task complete? {task[5]}
Description: {task[2]}
''')

    elif menu == 'e':
        """Exit the program."""
        print("Goodbye!!!")
        break

    else:
        """Handle invalid menu input."""
        print("You have entered an invalid input. Please try again.\n")


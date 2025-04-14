import datetime

# ==== Login Section ====
# Load usernames and passwords into a dictionary
users = {}
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(", ")
        users[username] = password

# Prompt user to log in
while True:
    user_name = input("Enter your username: ")
    user_pass = input("Enter your password: ")

    if user_name in users and users[user_name] == user_pass:
        print("Login successful!\n")
        break
    else:
        print("Invalid username or password. Try again.\n")

# ==== Menu ====
while True:
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()

    if menu == 'r':
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")
        confirm_pass = input("Confirm password: ")

        if new_pass == confirm_pass:
            with open("user.txt", "a") as f:
                f.write(f"\n{new_user}, {new_pass}")
            print("User registered successfully!\n")
        else:
            print("Passwords do not match. Try again.\n")

    elif menu == 'a':
        task_user = input("Enter username for task: ")
        title = input("Enter task title: ")
        desc = input("Enter task description: ")
        due_date = input("Enter due date (e.g. 20 Apr 2025): ")
        current_date = datetime.datetime.today().strftime("%d %b %Y")
        completed = "No"

        with open("tasks.txt", "a") as f:
            f.write(f"\n{task_user}, {title}, {desc}, {due_date}, {current_date}, {completed}")
        print("Task added successfully!\n")

    elif menu == 'va':
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip().split(", ")
                print(f'''
Task:        {task[1]}
Assigned to: {task[0]}
Date assigned: {task[4]}
Due date:   {task[3]}
Task complete? {task[5]}
Description: {task[2]}
''')

    elif menu == 'vm':
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip().split(", ")
                if task[0] == user_name:
                    print(f'''
Task:        {task[1]}
Assigned to: {task[0]}
Date assigned: {task[4]}
Due date:   {task[3]}
Task complete? {task[5]}
Description: {task[2]}
''')

    elif menu == 'e':
        print("Goodbye!!!")
        break

    else:
        print("Invalid option. Please try again.\n")

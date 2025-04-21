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
    if username == "admin":
        menu = input('''Select one of the following options:
r  - register a user                
a  - add task               
va - view all tasks                
vm - view my tasks
vc - view completed tasks
dt - delete task
ds - display statistics
gr - generate reports                 
e  - exit                
: ''').lower().strip()
    else:
        menu = input('''Select one of the following options:
 a - add task
 va - view all tasks
 vm - view my tasks 
 e - exit                    
:''').lower().strip()
    
    if menu == 'r' and username == 'admin':
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

    elif menu == 'vc' and username == 'admin':
        print("\nCompleted Tasks\n")
        with open('tasks.txt', 'r') as f:
            for line in f:
                task = line.strip().split(', ')
                if len(task) == 6 and task[5].lower == 'yes':
                    print(f'''
Task:        {task[1]}
Assigned to: {task[0]}
Date assigned: {task[4]}
Due date:   {task[3]}
Task complete? {task[5]}
Description: {task[2]}
''')
    elif menu == 'dt' and username == 'admin':
        print("\nDelete Task\n")
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
            
        for i, line in enumerate(tasks):
            task = line.strip().split(', ')
            if len(task) == 6:
                print(f"{i + 1}.{task[1]}(Assigned to {task[0]})")
                
        try: 
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                del tasks[task_num - 1]
                with open('tasks.txt', 'w') as f:
                    f.writelines(tasks)
                print("Task deleted.\n")
            else:
                print("Invalid task task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")
        
    elif menu == 'ds'and username == 'admin':
        with open('user.txt', 'r') as ufile:
            total_users = len(ufile.readlines())
        with open('tasks.txt', 'r') as tfile:
            total_tasks = len(tfile.readlines())
        print(f"\nStatistics\nUsers: {total_users}\nTasks: {total_tasks}\n")
       
    elif menu == 'gr' and username == 'admin':
        """Generate simple reports for admin."""
        with open('tasks.txt', 'r') as f:
            task_lines = f.readlines()

        total_tasks = len(task_lines)
        completed = 0
        incomplete = 0
        overdue = 0
        today = datetime.datetime.today()

        for line in task_lines:
            task = line.strip().split(', ')
            if len(task) == 6:
                if task[5].lower() == 'yes':
                    completed += 1
                else:
                    incomplete += 1
                    due_date = datetime.datetime.strptime(task[3], "%d %B %Y")
                    if due_date < today:
                        overdue += 1

        # Writing task overview
        with open('task_overview.txt', 'w') as f:
          print(f"Total tasks: {total_tasks}\n")
          print(f"Completed: {completed}\n")
          print(f"Incomplete: {incomplete}\n")
          print(f"Overdue: {overdue}\n")

        # Writing user overview
        with open('user_overview.txt', 'w') as f:
            f.write(f"Total users: {len(users)}\n")
            f.write(f"Total tasks: {total_tasks}\n")

        print("Reports generated.\n")

    elif menu == 'e':
        """Exit program"""
        print("Goodbye!\n")
        break

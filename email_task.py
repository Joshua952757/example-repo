# Email Simulator

# Email Class
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address 
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    def mark_as_read(self):
        self.has_been_read = True 
# Lists
inbox = []

def populate_inbox():
    sample_mails = [
        ("user1@gmail.com", "Meeting Reminder", "You're fired if you miss it."),
        ("user2@gmail.com", "Sale Alert!", "Don't be dumb and miss out on this discount."),
        ("user3@gmail.com", "Invitation", "You are invited to my funeral, yes I'm dead.")
    ]
    
    for email in sample_mails:
        inbox.append(Email(*email))

def list_emails():
    if not inbox:
        print("Inbox is empty.")
        return

    print("\nEmails in Inbox:")
    for i, email in enumerate(inbox):
        print(f"{i}: {email.subject_line}")    

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print("\n----- EMAIL -----")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        print("-----------------")
        email.mark_as_read()
    else:
        print("Invalid email index.")

def view_unread_emails():
    unread_emails = [email for email in inbox if not email.has_been_read]
    
    if not unread_emails:
        print("\nNo unread emails.")
    else:
        print("\nUnread Emails:")
        for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{i}: {email.subject_line}")

populate_inbox()

# Email program loop
while True:
    user_choice = input("""
Would you like to:
1. Read an email
2. View unread emails
3. Quit application
Enter selection:\n """)

    if user_choice == "1":
        list_emails()
        try:
            index = int(input("\nEnter the index of the email to read: "))
            read_email(index)
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    elif user_choice == "2":
        view_unread_emails()

    elif user_choice == "3":
        print("Exiting application.")
        break

    else:
        print("Invalid input. Please try again.")
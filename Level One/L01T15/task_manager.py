# L0T15 : CAPSTONE PROJECT


# INSTRUCTIONS : import the datetime module so i can get the current date when adding tasks
# open user.txt and read each line to get usernames and passwords
# for each line, split the line into username and password and store in a dictionary

# start a login loop to ask for username and password
#   check if the entered username exists and the password matches what's in the dictionary
#   if credentials are valid, break out of the login loop and continue to the main menu
#   if credentials are invalid, show an error and prompt again

# display the main menu with options: register user, add task, view all, view mine, or exit

# if the user selects 'r', check if they are the admin
#   if they are the admin, ask for a new username and password, then confirm the password
#   if confirmation matches, write the new credentials to user.txt
#   if the user is not admin, show a message denying access

# if the user selects 'a', prompt for task details: username, title, description, due date
#   get the current date and format it for writing
#   write all task details to tasks.txt, defaulting completion status to 'no'

# if the user selects 'va', open tasks.txt and read each task line by line
#   split each line into components and print them out in a formatted way

# if the user selects 'vm', open tasks.txt and loop through each task
#   check if the task is assigned to the currently logged-in user
#   if yes, print the task details in a formatted way

# if the user selects 'e', show a goodbye message
#   break the main loop to exit the program

# if the user enters something invalid, show an error and prompt again


# ===== importing libraries ============
from datetime import datetime

# ==== Login Section ====
# Open the user.txt file and load existing usernames and passwords
with open("user.txt", "r") as user_file:
    users = {}  # We'll store usernames and passwords in this dictionary
    for line in user_file:  # Loop through each line in the file
        username, password = line.strip().split(
            ", "
        )  # Split the line into username and password
        users[username] = password  # Add them to the dictionary

# Ask the user to log in until they enter valid credentials
while True:
    entered_username = input("Enter your username: ")  # Prompt for username
    entered_password = input("Enter your password: ")  # Prompt for password

    # Check if the entered username exists and the password matches
    if entered_username in users and users[entered_username] == entered_password:
        print("\nLogin successful!\n")  # Let the user know login worked
        break  # Exit the login loop
    else:
        print(
            "Invalid username or password. Please try again.\n"
        )  # Let the user retry if login fails

# Main loop to keep showing the menu until the user exits
while True:
    # Show the menu and ask for input, make it lowercase for consistency
    menu = input("""Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: """).lower()

    # If user chooses to register a new user
    if menu == "r":
        # Only admin is allowed to register new users
        if entered_username == "admin":
            new_username = input("Enter new username: ")  # Ask for new user's username
            new_password = input("Enter new password: ")  # Ask for new user's password
            confirm_password = input("Confirm password: ")  # Confirm password

            # Check if the password and confirmation match
            if new_password == confirm_password:
                with open("user.txt", "a") as user_file:  # Open the file in append mode
                    user_file.write(
                        f"\n{new_username}, {new_password}"
                    )  # Add new user credentials
                print("New user registered successfully!\n")  # Confirm success
            else:
                print(
                    "Passwords do not match. Try again.\n"
                )  # Warn if passwords didn't match
        else:
            print(
                "Only the admin can register new users.\n"
            )  # Restrict access to non-admin users

    # If user chooses to add a new task
    elif menu == "a":
        task_username = input(
            "Enter username to assign task to: "
        )  # Ask who the task is for
        task_title = input("Enter the title of the task: ")  # Ask for the task title
        task_description = input(
            "Enter a description of the task: "
        )  # Ask for task details
        task_due_date = input(
            "Enter the due date (e.g. 20 May 2025): "
        )  # Ask for due date
        assigned_date = datetime.now().strftime("%d %b %Y")  # Get today's date in correct format

        # Add the task to the tasks.txt file
        with open("tasks.txt", "a") as task_file:
            task_file.write(
                f"\n{task_username}, {task_title}, {task_description}, {assigned_date}, {task_due_date}, No"
            )

        print("Task successfully added!\n")  # Confirm task was saved

    # If user wants to view all tasks
    elif menu == "va":
        with open("tasks.txt", "r") as task_file:  # Open the tasks file for reading
            for line in task_file:  # Read each task
                task_data = line.strip().split(", ")  # Break line into parts
                print("\n--------------------------")  # Print separator for readability
                print(f"Task: {task_data[1]}")  # Task title
                print(f"Assigned to: {task_data[0]}")  # Who it's assigned to
                print(f"Date assigned: {task_data[3]}")  # When it was assigned
                print(f"Due date: {task_data[4]}")  # When it's due
                print(f"Task complete? {task_data[5]}")  # Whether it's done
                print(f"Description: {task_data[2]}")  # Task description
        print("\n")  # Print a newline after all tasks

    # If user wants to view only their tasks
    elif menu == "vm":
        with open("tasks.txt", "r") as task_file:  # Open tasks file
            for line in task_file:  # Loop through each line
                task_data = line.strip().split(", ")  # Break into parts
                if (
                    task_data[0] == entered_username
                ):  # Only show if it's assigned to current user
                    print("\n--------------------------")  # Print separator
                    print(f"Task: {task_data[1]}")  # Task title
                    print(f"Assigned to: {task_data[0]}")  # Assigned user
                    print(f"Date assigned: {task_data[3]}")  # Assignment date
                    print(f"Due date: {task_data[4]}")  # Due date
                    print(f"Task complete? {task_data[5]}")  # Completion status
                    print(f"Description: {task_data[2]}")  # Description
        print("\n")  # Add newline after displaying all tasks

    # If user chooses to exit the program
    elif menu == "e":
        print("Goodbye!!!")  # Say goodbye
        break  # Exit the while loop and end the program

    # Catch any invalid menu choices
    else:
        print(
            "You have entered an invalid input. Please try again\n"
        )  # Show error and retry

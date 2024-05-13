

# Plan out the code

# Empty Global Lists

incomplete_list = []
complete_list = []

# in our functions I am taking in an incomplete parameter that holds the place of incomplete_list and
# a complete parameter that holds the place of complete_list.
# So as to be consistent with good functions parameter naming conventions.
# When we call the driver code function, we fill in the global lists as arguments.




# Implement the following features:

# Add task
def add_task(incomplete):
    response = input("What would you like to add to your To-Do list? ").lower() #lower cases the string
    if response not in incomplete:
        incomplete.append(response)
        print(f"{response} has been added to your To Do list.")
    else:
        print(f"{response} is already in your To Do list.")

# view the list of tasks from:
#       incomplete          complete
def view_task(incomplete, complete):
    response = input("To view incomplete list type '1'; to view complete list type '2'. ")
    if response == "1":
        print(f"Incomplete list contains: {incomplete}.")
    elif response == "2":
        print(f"complete list contains: {complete}.")
    else:
        print("Please enter either '1' or '2' to view your lists.")

# marking a task as complete
def complete_task(incomplete, complete):
    response = input("To mark a task as complete, type 'complete a task'. Type 'quit' to quit.").lower()
    if response == "complete a task":
        response = input("What task would you like to mark as complete? ").lower()
        incomplete.remove(response)
        complete.append(response)
        print(f"Your completed List: {complete}")
    elif response == "quit":
        print("returning to previous menu.")
    elif ValueError:
        print("Not a valid response.")

# deleting a task
def del_task(incomplete, complete):
    response = input("To delete a task from 'incomplete' list, type 'incomplete'. To delete a task from 'complete' list, type 'complete'.")
    if response == "incomplete":
        incomplete.remove(response)
        print(f"Here is your new incomplete list: {incomplete}")
    elif response == "complete":
        complete.remove(response)
        print(f"{response} removed from completed list.")
    else: 
        ValueError
        print("Response not in a To Do list.")

# driver code
# command line interface

def run(incomplete, complete):
    while True:
        response = input("""\nWelcome to the To-Do List App!
    Enter a number from the following options.
    Menu: Pick one
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
        """)

        if response == "1":
            add_task(incomplete)
        elif response == "2":
            view_task(incomplete, complete)
        elif response == "3":
            complete_task(incomplete, complete)
        elif response == "4":
            del_task(incomplete, complete)
        elif response == "5":
            print("Now exiting the program.")
            break
        else:
            print("Please enter a number between 1 and 5.")

    run(incomplete_list, complete_list)
def display_menu():
    """Displays the menu options to the user."""

    print("Menu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user():
    """Displays a greeting message."""

    print("Hello! Welcome!")


def even_odd_checker_action():
    """Handles the even/odd check functionality."""

    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")


def handle_menu_choice(choice):
    """Handles the user's menu choice."""

    is_exit = False

    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        is_exit = True  # Signal to exit the program loop
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        is_exit = False  # Signal to continue the program loop

    return is_exit


# Main program flow
while True:
    display_menu()
    try:
        user_choice = int(input("Enter your choice (1-3): "))
        if handle_menu_choice(user_choice):
            break  # Exit the loop if handle_menu_choice signals to terminate
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
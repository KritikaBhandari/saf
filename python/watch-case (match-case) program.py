# a simple watch-case (match-case) program. It takes user input (1-3) and displays a corresponding message, with an option to exit
choice = input("Enter a number (1-3) to see a message or 'exit' to quit: ")

match choice:
    case "1":
        print("You selected option 1.")
    case "2":
        print("You selected option 2.")
    case "3":
        print("You selected option 3.")
    case "exit":
        print("Exiting program. Goodbye!")
    case _:
        print("Invalid choice! Please enter 1, 2, 3, or 'exit'.")

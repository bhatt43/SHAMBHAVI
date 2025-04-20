while True:
    user_input = input("Please enter an integer: ")
    try:
        number = int(user_input)
        print(f"Thank you! You entered the integer: {number}")
        break  # Exit the loop if input is valid
    except ValueError:
        print("Error: That was not an integer. Please try again.")

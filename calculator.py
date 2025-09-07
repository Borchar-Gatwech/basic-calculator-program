try:
    # Get the first number from the user
    num1 = float(input("Enter the first number: 10 "))

    # Get the second number from the user
    num2 = float(input("Enter the second number: 5 "))

    # Get the mathematical operation from the user
    operation = input("Enter the operation (+, -, *, /): + ")

    result = None

    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:  # Prevent division by zero
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter +, -, *, or /.")

    # Print the result if a valid operation was performed
    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")


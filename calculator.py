def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        # Prompt user to select an option
        choice = input("\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                # Taking inputs as numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                # Perform the selected operation
                if choice == '1':
                    print(f"The result of {num1} + {num2} is {num1 + num2}")
                elif choice == '2':
                    print(f"The result of {num1} - {num2} is {num1 - num2}")
                elif choice == '3':
                    print(f"The result of {num1} * {num2} is {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result of {num1} / {num2} is {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed!")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the calculator
calculator()

def show_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Select operation (1-5): ")

    if choice == "5":
        print("Exiting Calculator. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print("Result:", result)

            elif choice == "2":
                result = num1 - num2
                print("Result:", result)

            elif choice == "3":
                result = num1 * num2
                print("Result:", result)

            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print("Result:", result)
                else:
                    print("Error: Division by zero is not allowed.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select between 1-5.")

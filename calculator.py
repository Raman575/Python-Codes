def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"

def calculator():
    print("Welcome to the Calculator!")

    while True:
        print("\nPlease select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the Calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("The result of addition is:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("The result of subtraction is:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("The result of multiplication is:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("The result of division is:", result)
        else:
            print("Invalid input. Please try again.")

calculator()

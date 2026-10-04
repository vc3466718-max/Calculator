# Simple Calculator
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\n----- Calculator -----")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    operation = input("Enter operation: ")

    match operation:
        case "+":
            result = a + b

        case "-":
            result = a - b

        case "*":
            result = a * b

        case "/":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                result = a / b

        case _:
            print("Invalid operation.")

    if operation in ["+", "-", "*"] or (operation == "/" and b != 0):
        print(f"Result: {result}")

except ValueError:
    print("Please enter valid numbers.")
# Get input from user and convert to float
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter your operation (+, -, *, /): ")# Get the operation
    # Perform the operation
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return  num1 * num2
    elif operation == "/":    # Check for division by zero
        if num2 == 0:
           return  "Error: Division by zero!"
        else:
           return  num1 / num2
    else:
        return "Invalid operation. Please use +, -, *, or /."
    # Show the result
print("Result:", calculator())







    








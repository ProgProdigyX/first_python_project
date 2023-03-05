# This is my first Python script

def greet(name):
    """Greets the user with their name."""
    print(f"Hello, {name}!")

def calculate(num1, num2, operator):
    """Performs a mathematical operation on two numbers."""
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator!")
        return
    print(f"{num1} {operator} {num2} = {result}")

name = input("What's your name? ")
greet(name)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
calculate(num1, num2, operator)

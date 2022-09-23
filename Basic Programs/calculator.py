import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def clear():
    return os.system('cls')


def calculator():
    print("This is a calculator")

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if decision.upper() == 'Y':
            num1 = answer
        elif decision.upper() == 'N':
            should_continue = False
            clear()
            calculator()


calculator()
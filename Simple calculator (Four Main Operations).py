def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    num1 = float(input("What's the first number: "))

    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from above: ")

    num2 = float(input("What's the second number: "))

    if operation_symbol in operations:
        answer = float(f"{operations.get(operation_symbol)(num1, num2)}")
        print(f"{num1} {operation_symbol} {num2} = {answer}")


    cont_prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ").lower()

    while cont_prompt == "y":
        new_operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number: "))    
        if new_operation_symbol in operations:
            first_operand = answer
            answer = float(f"{operations.get(new_operation_symbol)(first_operand, num3)}")
            print(f"{first_operand} {new_operation_symbol} {num3} = {answer}")
            operation_symbol = new_operation_symbol
        cont_prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ").lower()
    else:
        calculator()

calculator()
def get_numbers(operation_string):
    """Splits the operation string into a list of numbers."""
    split_operation_list = operation_string.split()
    first_number = int(split_operation_list[0])
    operator = split_operation_list[1]
    second_number = int(split_operation_list[2])
    return first_number, operator, second_number


def calculate(first_number, operator, second_number):
    """Calculates the result of the operation."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        raise ValueError("Invalid operator")


def main():
    """The main function."""
    operation_string = input("Enter the calculation: ") #If you try any operation with double or more digits as operands, it will add a space between (66 -> 6 6). Same in line 38
    if " " not in operation_string:
        operation_string = operation_string.replace("", " ")

    while True:
        first_number, operator, second_number = get_numbers(operation_string)
        result = calculate(first_number, operator, second_number)
        print(f"{operation_string.strip()} = {result}")

        cont_prompt = input("Type 'yes' if you want to continue calculating with the result or type 'no' to start a new calculation: ").lower()
        if cont_prompt == "yes":
            operation_string = str(result) + " "
            operation_string_prompt = input(f"Enter the operator and the last operand only (e.g. * 5): {result} ") 
            if " " not in operation_string_prompt:
                operation_string_prompt = operation_string_prompt.replace("", " ").strip() 
            operation_string = operation_string + operation_string_prompt
            pass
        else:
           main()


main()

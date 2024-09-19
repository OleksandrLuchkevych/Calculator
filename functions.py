import math

def log_history(first_operand, operator, second_operand, result):
    with open('./source/history_log.txt', 'a') as file:
        file.write(f"{first_operand} {operator} {second_operand} = {result}\n")

def show_history():
    try:
        with open('./source/history_log.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "History is empty."

def input_number(numb):
    while True:
        try:
            return float(input(numb))
        except ValueError:
            print("Incorrect input! Please enter a number.")

def calculator(decimal_places):
    first_number = input_number("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /, ^, %): ")
    while operator not in ['+', '-', '*', '/','^','%','sq']:
        print("Invalid operator. Available operators: +, -, *, /.")
        operator = input("Enter operator (+, -, *, /, ^, sq, %): ")

    second_number = input_number("Enter the second number: ")
    if operator == '+':
        result = round(first_number + second_number, decimal_places)
    elif operator == '-':
        result = round(first_number - second_number, decimal_places)
    elif operator == '*':
        result = round(first_number * second_number, decimal_places)
    elif operator == '/':
        if second_number != 0:
            result = round(first_number / second_number, decimal_places)
        else:
            print("Error: division by zero!")
    elif operator == '^':
        result = round(first_number ** second_number, decimal_places)
    elif operator == '%':
        if second_number != 0:
            result = round(first_number % second_number, decimal_places)
        else:
            print("Error: division by zero!")

    if result is not None:
        log_history(first_number, operator, second_number, result)
        print(f"Result: {result}")
        return result
    else:
        return None

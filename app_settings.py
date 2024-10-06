decimal_places = 2
def set_decimal_places():
    global decimal_places
    while True:
        try:
            decimal_places = int(input("How many decimal places do you want to display? "))
            if decimal_places < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"Decimal places set to: {decimal_places}")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_decimal_places():
    return decimal_places

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operator(prompt):
    valid_operators = ['+', '-', '*', '/', '^', 'sq', '%']
    while True:
        operator = input(prompt)
        if operator in valid_operators:
            return operator
        print(f"Invalid operator! Choose from {valid_operators}.")

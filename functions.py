from app_settings import get_number, get_operator, get_decimal_places
from operations import addition, subtraction, multiplication, division, power, square_root, modulus
import memory as mh

class Calculator:
    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.operator = ''
        self.result = None

    def get_input(self):
        user_input = input("Enter the first number (or 'MR' to use memory): ").strip().upper()
        
        if user_input == 'MR':
            self.first_number = mh.recall_memory()
            print(f"Recalled from memory: {self.first_number}")
        else:
            try:
                self.first_number = float(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.first_number = get_number("Enter a valid first number: ")

        self.operator = get_operator("Enter the operator (+, -, *, /, ^, sq, %): ")
        
        user_input = input("Enter the second number (or 'MR' to use memory): ").strip().upper()
        
        if user_input == 'MR':
            self.second_number = mh.recall_memory()
            print(f"Recalled from memory: {self.second_number}")
        else:
            try:
                self.second_number = float(user_input)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                self.second_number = get_number("Enter a valid second number: ")

    def perform_operation(self):
        match self.operator:
            case '+':
                self.result = addition(self.first_number, self.second_number)
            case '-':
                self.result = subtraction(self.first_number, self.second_number)
            case '*':
                self.result = multiplication(self.first_number, self.second_number)
            case '/':
                self.result = division(self.first_number, self.second_number)
            case '^':
                self.result = power(self.first_number, self.second_number)
            case 'sq':
                self.result = square_root(self.first_number, self.second_number)
            case '%':
                self.result = modulus(self.first_number, self.second_number)

        formatted_result = f"{self.result:.{get_decimal_places()}f}"
        mh.log_history(self.first_number, self.operator, self.second_number, formatted_result)

    def display_result(self):
        if self.result is not None:
            formatted_result = f"{self.result:.{get_decimal_places()}f}"
            if self.operator == 'sq':
                print(f"The square root of {self.first_number} is {formatted_result}")
            else:
                print(f"{self.first_number} {self.operator} {self.second_number} = {formatted_result}")
        else:
            print("No result to display.")

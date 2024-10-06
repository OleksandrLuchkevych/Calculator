def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    while b == 0:
        print("You cannot divide by zero! Enter another number.")
        b = float(input("Enter second operand: "))
    return a / b

def power(a, b):
    return a ** b

def square_root(a, b):
    return a ** (1 / b)

def modulus(a, b):
    return a % b

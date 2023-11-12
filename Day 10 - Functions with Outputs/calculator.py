import os
from logo import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

flag = "n"

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

while True:
    if flag == "n":
        print(logo)
        first_number = float(input("What's the first number?: "))

        for key in operations:
            print(key)

    operator = input("Pick an operation: ")

    while operator not in ['+', '-', '*', '/']:
        print("Invalid operation!")
        operator = input("Pick an operation: ")

    second_number = float(input("What's the next number?: "))
    while operator == "/" and second_number == 0:
        print("Cannot divide by zero!")
        second_number = float(input("What's the next number?: "))

    result = operations[operator](first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")

    flag = input(
        f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    if flag == "n":
        os.system("cls || clear")
    elif flag == "y":
        first_number = result
    else:
        print("Wrong argument...Exiting...")
        break

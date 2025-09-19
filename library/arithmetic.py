# arithmetic.py
# This module contains basic arithmetic functions: addition, subtraction, division, and multiplication.
# Each function prompts the user for two numbers and prints the result of the operation.
# Functions do not return values; they directly print the results.
# The addition function
def add():
#   Prompt the user for two numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
#   Print the result of the two numbers
    print(float(num1) + float(num2))
# The subtraction function
def sub():
#   Prompt the user for two numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
#   Print the result of the two numbers
    print(float(num1) - float(num2))
# The division function
def div():
#   Prompt the user for two numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
#   Print the result of the two numbers
    print(float(num1) / float(num2))
# The multiplication function
def mul():
#   Prompt the user for two numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
#   Print the result of the two numbers
    print(float(num1) * float(num2))
# The help function
def help(*arithmetic):
#   If no arguments are provided, print a general help message
    if not arithmetic:
        print("Available functions: add, sub, div, mul")
        print("Use help(function_name) for more details.")
#   If specific functions are provided, print detailed help for each
    else:
        for func in arithmetic:
            match func:
                case "add":
                    print("add(): Prompts for two numbers and prints their sum.")
                case "add()":
                    print("add(): Prompts for two numbers and prints their sum.")                
                case "sub":
                    print("sub(): Prompts for two numbers and prints their difference.")
                case "sub()":
                    print("sub(): Prompts for two numbers and prints their difference.")
                case "div":
                    print("div(): Prompts for two numbers and prints their quotient.")
                case "div()":
                    print("div(): Prompts for two numbers and prints their quotient.")
                case "mul":
                    print("mul(): Prompts for two numbers and prints their product.")
                case "mul()":
                    print("mul(): Prompts for two numbers and prints their product.")
                case _:
                    print(f"No help available for {func}.")
if __name__ == "__main__":
    help()
    print(help(input("Enter function name for help: ")))
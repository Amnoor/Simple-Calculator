# Simple Calculator
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# The arithmetic functions are imported from a separate module named 'arithmetic.py'.
import arithmetic
# Display available operations
print("""What operation would you like?
+/Addition (A)
-/Subtraction (S)
//Division (D)
*/Multiplication (M)""")
# Get user input for the desired operation
operation = input("Enter operation: ")
# Match the input to the corresponding arithmetic function
match operation.lower():
    case "addition":
        print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "add":
        print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "plus":
        print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "a":
        print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "+":
        print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "subtraction":
        print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "minus":
        print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "s":
        print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "-":
        print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "division":
        print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "divide":
        print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "d":
        print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "/":
        print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "multiplication":
        print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "multiply":
        print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "times":
        print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "m":
        print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "*":
        print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
# Handle invalid operation input by prompting the user to try again
    case _:
        print("Invalid operation! Please try again!")
        is_error = True
        while is_error:
            operation = input("Enter operation: ")
            match operation.lower():
                case "addition":
                    print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "add":
                    print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "plus":
                    print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "a":
                    print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "+":
                    print(arithmetic.add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "subtraction":
                    print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "minus":
                    print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "s":
                    print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "-":
                    print(arithmetic.sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "division":
                    print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "divide":
                    print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "d":
                    print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "/":
                    print(arithmetic.div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "multiplication":
                    print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                case "multiply":
                    print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "times":
                    print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "m":
                    print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "*":
                    print(arithmetic.mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
# If the input is still invalid, continue prompting the user
                case _:
                    print("Invalid operation! Please try again!")
                    is_error = True
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
        arithmetic.add()
    case "add":
        arithmetic.add()
    case "plus":
        arithmetic.add()
    case "a":
        arithmetic.add()
    case "+":
        arithmetic.add()
    case "subtraction":
        arithmetic.sub()
    case "minus":
        arithmetic.sub()
    case "s":
        arithmetic.sub()
    case "-":
        arithmetic.sub()
    case "division":
        arithmetic.div()
    case "divide":
        arithmetic.div()
    case "d":
        arithmetic.div()
    case "/":
        arithmetic.div()
    case "multiplication":
        arithmetic.mul()
    case "multiply":
        arithmetic.mul()
    case "times":
        arithmetic.mul()
    case "m":
        arithmetic.mul()
    case "*":
        arithmetic.mul()
# Handle invalid operation input by prompting the user to try again
    case _:
        print("Invalid operation! Please try again!")
        is_error = True
        while is_error:
            operation = input("Enter operation: ")
            match operation.lower():
                case "addition":
                    arithmetic.add()
                    is_error = False
                case "add":
                    arithmetic.add()
                    is_error = False
                case "plus":
                    arithmetic.add()
                    is_error = False
                case "a":
                    arithmetic.add()
                    is_error = False
                case "+":
                    arithmetic.add()
                    is_error = False
                case "subtraction":
                    arithmetic.sub()
                    is_error = False
                case "minus":
                    arithmetic.sub()
                    is_error = False
                case "s":
                    arithmetic.sub()
                    is_error = False
                case "-":
                    arithmetic.sub()
                    is_error = False
                case "division":
                    arithmetic.div()
                    is_error = False
                case "divide":
                    arithmetic.div()
                    is_error = False
                case "d":
                    arithmetic.div()
                    is_error = False
                case "/":
                    arithmetic.div()
                    is_error = False
                case "multiplication":
                    arithmetic.mul()
                case "multiply":
                    arithmetic.mul()
                    is_error = False
                case "times":
                    arithmetic.mul()
                    is_error = False
                case "m":
                    arithmetic.mul()
                    is_error = False
                case "*":
                    arithmetic.mul()
                    is_error = False
# If the input is still invalid, continue prompting the user
                case _:
                    print("Invalid operation! Please try again!")
                    is_error = True
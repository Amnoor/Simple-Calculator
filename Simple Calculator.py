# I am gonna make a simple calculator.
import arithmetic
# asking the user for what operation.
print("""What operation would you like?
+/Addition (A)
-/Subtraction (S)
//Division (D)
*/Multiplication (M)""")
operation = input("Enter operation: ")
# depending on the operation, the program will ask what number to add, subtract, divide, or Multiply, then print the result.
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
# if the user types or do something that can't be done instead of the program crashing it will just print out "Invalid operation! Please try again!" and make the user try again.
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
                case _:
                    print("Invalid operation! Please try again!")
                    is_error = True
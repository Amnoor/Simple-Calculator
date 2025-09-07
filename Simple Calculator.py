# I am gonna make a simple calculator.
# asking the user for what operation.
print("""What operation would you like?
+/Addition (A)
-/Subtraction (S)
//Division (D)
*/Multiplication (M)""")
operation = input("Enter operation: ")
# depending on the operation, the program will ask what number to add, subtract, divide, or Multiply, then print the result.
if operation.lower() == "addition":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 + num2
    print(f"{result:,}")
elif operation.lower() == "a":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 + num2
    print(f"{result:,}")
elif operation == "+":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 + num2
    print(f"{result:,}")
elif operation.lower() == "subtraction":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 - num2
    print(f"{result:,}")
elif operation.lower() == "s":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 - num2
    print(f"{result:,}")
elif operation == "-":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 - num2
    print(f"{result:,}")
elif operation.lower() == "division":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 / num2
    print(f"{result:,}")
elif operation.lower() == "d":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 / num2
    print(f"{result:,}")
elif operation == "/":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 / num2
    print(f"{result:,}")
elif operation.lower() == "multiplication":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 * num2
    print(f"{result:,}")
elif operation.lower() == "m":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 * num2
    print(f"{result:,}")
elif operation == "*":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    result = num1 * num2
    print(f"{result:,}")
# if the user types or do something that can't be done instead of the program crashing it will just print out "Invalid operation! Please try again!" and make the user try again.
else:
    print("Invalid operation! Please try again!")
    is_error = True
    while is_error:
        operation = input("Enter operation: ")
        if operation.lower() == "addition":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 + num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "a":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 + num2
            print(f"{result:,}")
            is_error = False
        elif operation == "+":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 + num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "subtraction":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 - num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "s":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 - num2
            print(f"{result:,}")
            is_error = False
        elif operation == "-":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 - num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "division":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 / num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "d":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 / num2
            print(f"{result:,}")
            is_error = False
        elif operation == "/":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 / num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "multiplication":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 * num2
            print(f"{result:,}")
            is_error = False
        elif operation.lower() == "m":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 * num2
            print(f"{result:,}")
            is_error = False
        elif operation == "*":
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            result = num1 * num2
            print(f"{result:,}")
            is_error = False
        else:
            print("Invalid operation! Please try again!")
            is_error = True
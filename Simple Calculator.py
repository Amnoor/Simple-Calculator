# I am gonna make a simple calculator.
# asking the user for what operation.
print("""What operation would you like?
+/Addition (A)
-/Subtraction (S)
//Division (D)
*/Multiplication (M)""")
operation = input("Enter your operation: ")
# depending on the operation, the program will ask what number to add, subtract, divide, or Multiply, then print the result.
if operation.lower() == "addition":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 + num2
    print(f"{result:,}")
elif operation.lower() == "a":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 + num2
    print(f"{result:,}")
elif operation == "+":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 + num2
    print(f"{result:,}")
elif operation.lower() == "subtraction":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 - num2
    print(f"{result:,}")
elif operation.lower() == "s":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 - num2
    print(f"{result:,}")
elif operation == "-":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 - num2
    print(f"{result:,}")
elif operation.lower() == "division":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 / num2
    print(f"{result:,}")
elif operation.lower() == "d":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 / num2
    print(f"{result:,}")
elif operation == "/":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 / num2
    print(f"{result:,}")
elif operation.lower() == "multiplication":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 * num2
    print(f"{result:,}")
elif operation.lower() == "m":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 * num2
    print(f"{result:,}")
elif operation == "*":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    result = num1 * num2
    print(f"{result:,}")
# if the user types or do something that can't be done instead of the program crashing it will just print out "Invalid operation! Please try again later.".
else:
    print("Invalid operation! Please try again later.")
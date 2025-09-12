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
    def add(num1, num2):
        return num1 + num2
    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "add":
    def add(num1, num2):
        return num1 + num2
    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "plus":
    def add(num1, num2):
        return num1 + num2
    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "a":
    def add(num1, num2):
        return num1 + num2
    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation == "+":
    def add(num1, num2):
        return num1 + num2
    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "subtraction":
    def sub(num1, num2):
        return num1 - num2
    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "minus":
    def sub(num1, num2):
        return num1 - num2
    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "s":
    def sub(num1, num2):
        return num1 - num2
    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation == "-":
    def sub(num1, num2):
        return num1 - num2
    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "division":
    def div(num1, num2):
        return num1 / num2
    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "divide":
    def div(num1, num2):
        return num1 / num2
    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "d":
    def div(num1, num2):
        return num1 / num2
    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation == "/":
    def div(num1, num2):
        return num1 / num2
    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "multiplication":
    def mul(num1, num2):
        return num1 * num2
    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "multiply":
    def mul(num1, num2):
        return num1 * num2
    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "times":
    def mul(num1, num2):
        return num1 * num2
    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation.lower() == "m":
    def mul(num1, num2):
        return num1 * num2
    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
elif operation == "*":
    def mul(num1, num2):
        return num1 * num2
    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
# if the user types or do something that can't be done instead of the program crashing it will just print out "Invalid operation! Please try again!" and make the user try again.
else:
    print("Invalid operation! Please try again!")
    is_error = True
    while is_error:
        operation = input("Enter operation: ")
        if operation.lower() == "addition":
            def add(num1, num2):
                return num1 + num2
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "add":
            def add(num1, num2):
                return num1 + num2
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "plus":
            def add(num1, num2):
                return num1 + num2
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "a":
            def add(num1, num2):
                return num1 + num2
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation == "+":
            def add(num1, num2):
                return num1 + num2
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "subtraction":
            def sub(num1, num2):
                return num1 - num2
            print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "minus":
            def sub(num1, num2):
                return num1 - num2
            print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "s":
            def sub(num1, num2):
                return num1 - num2
            print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation == "-":
            def sub(num1, num2):
                return num1 - num2
            print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "division":
            def div(num1, num2):
                return num1 / num2
            print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "divide":
            def div(num1, num2):
                return num1 / num2
            print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "d":
            def div(num1, num2):
                return num1 / num2
            print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation == "/":
            def div(num1, num2):
                return num1 / num2
            print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "multiplication":
            def mul(num1, num2):
                return num1 * num2
            print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "multiply":
            def mul(num1, num2):
                return num1 * num2
            print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "times":
            def mul(num1, num2):
                return num1 * num2
            print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation.lower() == "m":
            def mul(num1, num2):
                return num1 * num2
            print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        elif operation == "*":
            def mul(num1, num2):
                return num1 * num2
            print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
            is_error = False
        else:
            print("Invalid operation! Please try again!")
            is_error = True
# I am gonna make a simple calculator.
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
        def add(num1, num2):
            return num1 + num2
        print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "add":
        def add(num1, num2):
            return num1 + num2
        print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "plus":
        def add(num1, num2):
            return num1 + num2
        print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "a":
        def add(num1, num2):
            return num1 + num2
        print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "+":
        def add(num1, num2):
            return num1 + num2
        print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "subtraction":
        def sub(num1, num2):
            return num1 - num2
        print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "minus":
        def sub(num1, num2):
            return num1 - num2
        print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "s":
        def sub(num1, num2):
            return num1 - num2
        print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "-":
        def sub(num1, num2):
            return num1 - num2
        print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "division":
        def div(num1, num2):
            return num1 / num2
        print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "divide":
        def div(num1, num2):
            return num1 / num2
        print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "d":
        def div(num1, num2):
            return num1 / num2
        print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "/":
        def div(num1, num2):
            return num1 / num2
        print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "multiplication":
        def mul(num1, num2):
            return num1 * num2
        print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "multiply":
        def mul(num1, num2):
            return num1 * num2
        print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "times":
        def mul(num1, num2):
            return num1 * num2
        print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "m":
        def mul(num1, num2):
            return num1 * num2
        print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
    case "*":
        def mul(num1, num2):
            return num1 * num2
        print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
# if the user types or do something that can't be done instead of the program crashing it will just print out "Invalid operation! Please try again!" and make the user try again.
    case _:
        print("Invalid operation! Please try again!")
        is_error = True
        while is_error:
            operation = input("Enter operation: ")
            match operation.lower():
                case "addition":
                    def add(num1, num2):
                        return num1 + num2
                    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "add":
                    def add(num1, num2):
                        return num1 + num2
                    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "plus":
                    def add(num1, num2):
                        return num1 + num2
                    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "a":
                    def add(num1, num2):
                        return num1 + num2
                    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "+":
                    def add(num1, num2):
                        return num1 + num2
                    print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "subtraction":
                    def sub(num1, num2):
                        return num1 - num2
                    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "minus":
                    def sub(num1, num2):
                        return num1 - num2
                    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "s":
                    def sub(num1, num2):
                        return num1 - num2
                    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "-":
                    def sub(num1, num2):
                        return num1 - num2
                    print(sub(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "division":
                    def div(num1, num2):
                        return num1 / num2
                    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "divide":
                    def div(num1, num2):
                        return num1 / num2
                    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "d":
                    def div(num1, num2):
                        return num1 / num2
                    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "/":
                    def div(num1, num2):
                        return num1 / num2
                    print(div(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "multiplication":
                    def mul(num1, num2):
                        return num1 * num2
                    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                case "multiply":
                    def mul(num1, num2):
                        return num1 * num2
                    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "times":
                    def mul(num1, num2):
                        return num1 * num2
                    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "m":
                    def mul(num1, num2):
                        return num1 * num2
                    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case "*":
                    def mul(num1, num2):
                        return num1 * num2
                    print(mul(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
                    is_error = False
                case _:
                    print("Invalid operation! Please try again!")
                    is_error = True
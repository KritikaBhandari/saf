while True:
    print("Simple Calculator")
    print("Enter two numbers and an operator (+, -, *, /)")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid operator! Please enter one of +, -, *, or /")
    
    cont = input("Type 'stop' to exit or press Enter to continue: ")
    if cont.lower() == 'stop':
        break

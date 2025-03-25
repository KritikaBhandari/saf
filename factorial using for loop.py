while True:
    num = int(input("Enter a number to find its factorial: "))
    fact = 1
    
    for i in range(1, num + 1):
        fact *= i
    
    print("Factorial:", fact)
    
    cont = input("Type 'stop' to exit or press Enter to continue: ")
    if cont.lower() == 'stop':
        break

def simple_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    time = float(input("Enter time (in years): "))
    interest = (principal * rate * time) / 100
    print("Simple Interest:", interest)

simple_interest()

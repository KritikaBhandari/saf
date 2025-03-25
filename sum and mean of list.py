numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

if numbers:
    total = sum(numbers)
    mean = total / len(numbers)
    print("Sum:", total)
    print("Mean:", mean)
else:
    print("No numbers entered!")

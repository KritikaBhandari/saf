"""rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print(" ".join(str(num) for num in range(1, i + 1)))"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

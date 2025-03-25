try:
    num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    index = int(input("Enter an index to access: "))
    print("Value at index:", num_list[index])
except (IndexError, ValueError) as e:
    print("Error:", e)
finally:
    print("Execution completed.")


#This will stop the program and raise a ValueError with the message "Negative numbers are not allowed!
"""x = -5
if x < 0:
    raise ValueError("Negative numbers are not allowed!")
"""
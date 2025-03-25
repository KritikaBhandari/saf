try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")


"""try:
    num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    index = int(input("Enter an index to access: "))
    print("Value at index:", num_list[index])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid input! Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
"""
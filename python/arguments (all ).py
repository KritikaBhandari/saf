import sys

# Positional Arguments
def add_numbers(a, b):
    return a + b

# Keyword Arguments
def greet(name="User"):
    print(f"Hello, {name}!")

# Default Arguments
def power(base, exponent=2):
    return base ** exponent

# Variable-length Arguments (*args)
def calculate_sum_and_mean(*args):
    if args:
        total = sum(args)
        mean = total / len(args)
        print("Sum:", total)
        print("Mean:", mean)
    else:
        print("No numbers provided!")

# Keyword Variable-length Arguments (**kwargs)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
   # Testing different types of arguments
    print("# Positional Arguments")
    print("Sum:", add_numbers(3, 5))
    
    print("\n# Keyword Arguments")
    greet(name="kritika")
    
    print("\n# Default Arguments")
    print("Power:", power(3))
    print("Power with custom exponent:", power(3, 4))
    
    print("\n# Variable-length Arguments")
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    calculate_sum_and_mean(*numbers)
    
    print("\n# Keyword Variable-length Arguments")
    display_info(Name="kritika", Age=18, Country="india")
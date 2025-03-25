"""def fibonacci_series(n):
    if n <= 0:
        return "Invalid input"
    series = [fibonacci(i) for i in range(1, n + 1)]
    return series

# Example usage
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_series(n))"""


def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

n = int(input("Enter the number of terms: "))
print(fibonacci_recursive(n))


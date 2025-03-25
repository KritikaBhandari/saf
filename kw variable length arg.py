def print_details(**kwargs):
    print("Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_details(Name="Alice", Age=22, Country="India")

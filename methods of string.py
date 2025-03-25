text = input("Enter a string: ")

# Convert to uppercase
print("Uppercase:", text.upper())

# Convert to lowercase
print("Lowercase:", text.lower())

# Remove leading and trailing spaces
print("Stripped:", text.strip())

# Replace a substring
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("Replaced:", text.replace(old, new))

# Split into a list
separator = input("Enter a separator: ")
print("Split:", text.split(separator))

# Join elements of a list
words = input("Enter words separated by space: ").split()
print("Joined:", "#".join(words))

# Find a substring
substring = input("Enter substring to find: ")
print("First occurrence at index:", text.find(substring))

# Count occurrences of a substring
count_sub = input("Enter substring to count: ")
print("Count:", text.count(count_sub))

# Check start and end of string
start_sub = input("Enter starting substring: ")
print("Starts with:", text.startswith(start_sub))

end_sub = input("Enter ending substring: ")
print("Ends with:", text.endswith(end_sub))

# Capitalize first letter
print("Capitalized:", text.capitalize())

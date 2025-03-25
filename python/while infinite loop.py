"""i = 1
while i > 0:
    print("This is an infinite loop!")"""

while True:
    user_input = input("Type 'stop' to end the loop: ")
    if user_input.lower() == 'stop':
        break
    print("This is an infinite loop!")

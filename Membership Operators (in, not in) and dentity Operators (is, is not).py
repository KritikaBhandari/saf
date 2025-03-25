#Membership Operators (in, not in)
my_list = [1, 2, 3, 4, 5]

print(3 in my_list)     # True (3 is in the list)
print(6 not in my_list) # True (6 is not in the list)

#identity Operators (is, is not)
a = [10, 20, 30]
b = a  
c = [10, 20, 30]

print(a is b)      # True (b refers to the same object as a)
print(a is c)      # False (c is a different object with the same values)
print(a is not c)  # True (a and c are different objects)

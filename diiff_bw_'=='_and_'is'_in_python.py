a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True, as the content of 'a' and 'b' are equal
print(a == c)  # True, as the content of 'a' and 'c' are equal


a1 = [1, 2, 3]
b1 = [1, 2, 3]
c1 = a1

print(a1 is b1)  # False, as 'a' and 'b' reference different objects
print(a1 is c1)  # True, as 'a' and 'c' reference the same object

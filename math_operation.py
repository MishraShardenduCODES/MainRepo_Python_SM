import math
a=3.14

print(math.trunc(a))   # Output: 3
print(math.trunc(-3.9))  # Output: -3


print(round(3.14159, 2))  # Output: a (rounds to 2 decimal places)
print(round(123.656, -1))  # Output: 120.0 (rounds to the nearest tens place)

print(math.floor(a))   # Output: 3
print(math.floor(-a))  # Output: -4

print(math.ceil(a))   # Output: 4
print(math.ceil(-a))  # Output: -3
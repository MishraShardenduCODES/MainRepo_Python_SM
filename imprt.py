import math 

result = math.sqrt(9)*math.pi
print(result)  # Output: 3.0


from math import sqrt, pi

result = sqrt(49) * pi
print(result)  # Output: ~ 22


from math import *

result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793


import math as m

result = m.sqrt(9)
print(result)  # Output: 3.
print(m.pi)  # Output: 3.141592653589793

print(dir(math))
print(math.nan,type(math.nan))

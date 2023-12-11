# THIS IS BECAUSE A AND B HAVE SAME VALUE # 
# THIS IS BECAUSE PYTHON DEOSEN'T GIVE A CONSTANT DIFFERENT LOCATION OF ADDRESS #
a = 2
b = 2
print(a is b)
print(a == b)

# THIS IS AS NONE HAS SAME ADDRESS NO MATTER WHICH VALUE IS IT ASSIGNED TO #
a = None
b = None
print(a is b)
print(a == b)

# SAME AS NONE AND CONSTANT VALUES #
a = "hELLO"
b = "hELLO"
print(a is b)
print(a == b)

# NOT APPLICABLE ON LIST AND TUPLE #
a = (1,2,3,4)
b = (1,2,3,4)
print(a is b)
print(a == b)

a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)
print(a == b)
# HOW map(function,iterable) FUNCTION WORKS #
sqr = lambda x : x**2
num = [1,2,3,4,5,6]
sqr_lst = map(sqr,num)
print(sqr_lst)        # This doesen't return list you have to donvert it to a list #
print(list(sqr_lst))

# # # # # # # # # # # # # # # #
#  this is same as :          #
#  l = [1, 2, 4, 6, 4, 3]     #
#  newl = []                  #
#  for item in l:             #
#    newl.append(cube(item))  #
# # # # # # # # # # # # # # # #
 
# HOW filter(function,iterable) FUNCTION WORKS #
num2 = [1,14,2,4,5,67,23,54,7,8,6,3,1,0]
def fltr_fnc(a) :
    return a>5 
num2 = list(filter(fltr_fnc,num2))
print(num2)

# HOW reduce(function,iterable) FUNCTION WORKS #
from functools import reduce
num1 = [1,2,3,4,5,6,7,8]
def prd(x,y) :
    return x*y 
num = float(reduce(prd,num1)) 
print(num)
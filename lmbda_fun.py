# SYNTAX : lambda arguments: expression
sqr = lambda x : x**2 
cube = lambda x : x**3
prd = lambda x,y : f"float({x:.2f}) x float({y:.2f}) = float({x:.2f})*float({y:.2f} "

x = float(input("Tell first number  : "))
y = float(input("Tell second number : "))

print(f"The square of {x:.2f} is : {sqr(x):.2f}")
print(f"The square of {y:.2f} is : {sqr(y):.2f}")
print(f"The cube of {x:.2f} is : {cube(x):.2f}")
print(f"The cube of {y:.2f} is : {cube(y):.2f}")
print(f"The Product of {x:.2f} and {y:.2f} : {(x*y):.2f}")
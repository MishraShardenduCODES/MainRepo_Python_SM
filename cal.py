a = input("Tell the operation: ")
b = float(input("Tell first number: "))
c = float(input("Tell second number: "))

if a == "+":
    print("The sum of b and c = %f ", b + c)
elif a == "-":
    print("The difference of b and c =", b - c)
elif a == "*":
    print("The product of b and c =", b * c)
elif a == "/":
    if c == 0:
        print("Division by 0 is not possible")
    else:
        print("The division gives:", b / c)
else:
    print("Invalid operation")

def fact(a):
    '''This is a function to calculate factorial'''
    if ( a == 0 ):
        return 1    
    else :
        return a*fact(a-1)

a = int(input("Tell a number : "))
print(fact.__doc__)
print(fact(a))

def fibo(a):
    
    if ( a <= 1 ):
        return a
    else :
        return fibo(a-1) + fibo(a-2)

print("The digit in fibonaaci sequence is : ",fibo(int(input("Tell how many digits in the sequence you want : "))-1))

# default and keyword arguments 
def avg1(a = 5,b = 4):
    sum = 0
    print((a+b)/2)
avg1()
avg1(b = 4,a = 6)

#required arguments 
def avg2( a , b , c ):
   print((a+b+c)/3)

avg2(5,1,4)

#variable arguments 
def avg(*numbers):
    total = 0 
    for i in numbers :
        total += i
    # total = sum(numbers) also does teh job without loop
    print(total/len(numbers))

num_lst = [2,5,4,6,8]
avg(*num_lst)

def dct(**info):
    for key,value in info.items():
        print(f" {key} : {value} ", end = '\b,'  )
    print('\b    ')
dct ( name = "Shardendu" , age = 19 , marks = 98.43) 

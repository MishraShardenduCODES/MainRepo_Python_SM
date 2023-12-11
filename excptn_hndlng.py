x = input("Tell an integral value : ")

try :
    for i in range(10) : 
        print(f"{int(x)} x {i} = {int(x)*i} ")

except Exception as y :
    print(y)
print('THIS CODE IS WRITTEN TO TELL HOW EXCEPTION HANDELLING WORKS',end = '\n\n')


a = input("Tell an integral value : ")
try :
    for i in range ( int(a) ) :
        if i % 2 == 0 :
            print(i)
    
    ls = [12,42,73,84,95,61,73,58,79,10]
    print(f"The element at {(int(a))} index in the list is : {ls[(int(a))]}")

except ValueError :
    print("You did not enter an Integral Value !!!!")

except IndexError : 
    print("The value of this index doesent exist in list !!!!")

# THIS CODE WE SEE HOW ERROR HANDELING WORKS #
# ENTER =>
# x = str and y = str
# x = 5 and y = 23

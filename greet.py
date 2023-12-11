def greet( name = 'Shardendu Mishra' , age = 19 , branch = ' C.S.E ' ):
    return ' Hi ' + name + " you're " + str(age) + ' y/o ' + ' from ' + branch + ' branch1 '


#using for loop  
a=int(input('Tell how many people you wanna greet : '))
for i in range (a):
    name = str(input("Tell you're name : "))
    age = int(input("Tell you're age : "))
    branch = str(input("Tell you're Branch : "))
    print(greet(name , age , branch ) , end =  '\n')

#using while loop 
i=0
while  ( i < a ) :
    name = str(input("Tell you're name : "))
    age = int(input("Tell you're age : "))
    branch = str(input("Tell you're Branch : "))
    print(greet(name , age , branch ) , end =  '\n')
    i += 1

def say_bye( name = 'Shardendu Mishra' , age = 19 , branch = ' C.S.E ' ) :
    pass 

# if pass is not used it will throw an error #
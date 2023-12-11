
# This is a code to represent match case in Python 
# - By Shardendu Mishra 


num1 = float(input("Tell first number : "))
num2 = float(input("Tell second number : "))

a = str(input("Tell the case you want to operate ( + , - , / , || , // , * ) : "))
b = num1-num2  
match a:
    case '+' : 
        print("The sum is given by : ", num1+num2)    
    case '-' :
        print("The difference is given by : ", b )
    case '||' :
        print("The mod of both number is :",abs(num1)," and ",abs(num2)," and the mod of there difference is given by : ", abs(b) )
    case '*' :
        print("The product is given by : ", num1*num2)
    case '/' :
        if( num2 == 0 ) :
            print("Divison by 0 is not possible the answer tends to infinity ")
        else :
            print("The division of the two number gives : ", num1/num2)
    case '//' :
        if( num2 == 0 ) :
            print("Floor Divison by 0 is not possible the answer tends to infinity ")
        else :
            print("The floor division of the two number gives : ", num1//num2)
    case default if a == '>' :
        print("The bigeer number of the two is : ",max(num1,num2))
    case default if a == '<' :
        print("The smaller number of the two is : ",min(num1,num2))
    case default if (a == '==' or a == '!=') :
        if( num1 == num2 ) :
            print("The number ", num1 , "and the number ", num2 ," are equal ")
        else : 
            print("The number ", num1 , "and the number ", num2 ," are not equal ")


# This code doesent work in my vs code and throws an error though the interpreter in 3.12.0
# When I write python --version it still shows the old 3.6 version even though I have installed the new version
# The `match` statement was introduced in Python 3.10. Therefore,
# if you are using Python 3.6.4rc1, which predates Python 3.10, 
# the `match` statement will not work, and attempting to use it will result in a syntax error.
# To use the `match` statement, you'll need Python 3.10 or a higher version. 
# If you're working with an older Python version like 3.6.4rc1, 
# you'll need to use alternative control flow statements like `if`, `elif`, and `else` for similar functionality instead of `match`.
import time
timestamp = time.strftime(' %H : %M : %S ')
print("The currently is : ",timestamp)
hour = int(time.strftime("%H")) 

if ( hour >= 23 or hour <= 6 ) :
    print("It's too early go back to sleep !!!!")
elif ( hour > 6 and hour <= 12 ) :
    print("Good Morning !!")
elif ( hour > 12 and hour <= 18 ) :
    print("Good Afternoon !!")
else:
    print("Good evening !!") 
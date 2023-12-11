import random as rd


a = str(input("Tell what do you want to choose (Snake, Water or Gun) : "))
a = a.lower()
if( a == 'snake' ):
    b = 0
elif( a == 'water' ):
    b = 1
elif( a == 'gun' ):
    b = 2
else :
    print("This is not Valid Option")


c = rd.randint(0,2)
if( c == 0 ):
    str = 'snake'
elif( c == 1 ):
    str = 'water'
elif( c == 2 ):
    str = 'gun'


# #            snake    water    gun
# #      a :     0        1       2 
# #   b : 
# snake 0      drew     lost    won
# water 1      won      drew    lost
# gun   2      lost     won     drew


result = [['drew','lost','won'] , ['won','drew','lost'] , ['lost','won','drew']]
print(f"You chose \'{a.upper()}\' and computer choose \'{str.upper()}\' so you : {result[b][c].upper()}")

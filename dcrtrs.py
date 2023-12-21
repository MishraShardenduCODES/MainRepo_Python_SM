def greet(fx):
    def mfx (*args,**kwargs):
        print('Good Morning !!')
        fx(*args,**kwargs)
        # *args This intakes a tuplele and **kwargs This intakes a dictionary
        print('Thanks for using this function !!')
    return mfx

@greet
def hello():
    print("Hello !!!!")

@greet
def add(x,y):
    print('The addition of x and y = ',x + y)

hello()
x = int(input("Tell first  number : ")) 
y = int(input("Tell second number : "))
add(x,y)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# __init__ method #

class Student :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    def show(self) :
        print(f"Hi I am {self.name} and you're age is {self.age}")

std1 = Student("Shardendu Mishra",20)
std1.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# __str__ and __repr__ method #
class Student :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    def __str__(self) :
        return f"Name : {self.name} , Age : {self.age}"
    def __repr__(self) :
        return f"Name : {self.name} , Age : {self.age}"

std = Student("Shardendu Mishra",20)
print(str(std))
print(repr(std))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# __len__ method #
class Student :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    def __len__(self) :
        len = 0
        for i in self.name :
            len += 1
        return len 
    
std1 = Student("Shardendu Mishra",20)
length = len(std1)
print(f"The length of this string is : {length}") 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# __call__ method #
class Student :
    def __init__(self,name,cmp) :
        self.name = name
        self.cmp = cmp
    def __call__(self) :
        print(f"Hi {self.name} how are you ?")

std = Student("Shardendu Mishra","Apple")
std()

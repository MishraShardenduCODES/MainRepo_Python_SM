# This is a single program to make show different DUNDER/MAGIC METHODS #
class Student :
    
    def __init__(self,name,age,cmp) :
        self.name = name 
        self.age = age 
        self.cmp = cmp
    
    def show(self) :
        print(f"Hi I am {self.name} and you're age is {self.age}")
    
    def __str__(self) :
        return f"Name : {self.name} , Age : {self.age}"
    
    def __repr__(self) :
        return f"Name : {self.name} , Age : {self.age}"
    
    def __len__(self) :
        len = 0
        for i in self.name :
            len += 1
        return len
    
    def __call__(self) :
        print(f"Hi {self.name} how are you ?")


std = Student("Shardendu Mishra",20,"Apple")
std.show()
print(str(std))
print(repr(std))
print(f"The length of this string is : {len(std)}")
std()
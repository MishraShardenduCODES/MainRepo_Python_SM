# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Employee :
    cmp = "Apple"
    def show(self) :
        print(f"The Name is {self.name} and the company is {self.cmp}")

    @classmethod
    def chngcmp(cls,newcmp) :
        cls.cmp = newcmp

e1 = Employee()
e1.name = "Mishra"
e1.show()

# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Employee :
    def __init__(self,name,cmp):
        self.name = name 
        self.cmp = cmp 

    def show(self) :
        print(f"The Name is {self.name} and the company is {self.cmp}")

    @classmethod
    def chngcmp(cls,newcmp) :
        cls.cmp = newcmp

e1 = Employee("Shardendu Mishra","Tesla")
e1.show()

# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
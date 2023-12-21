# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Parent :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age

    def show(self) :
        print(f"The name of the guy is {self.name} and you're age is {self.age}")
    
class child(Parent) :
    def __init__(self,name,age,id,lang) :
        self.id = id
        self.lang = lang
        super().__init__(name,age)

    def show(self) :
        print(f"The name of the guy is {self.name} and you're age is {self.age} ur id is {self.id} and u know {self.lang}")


rohan = Parent("Rohan",19)
rohan.show()

Mishra = child("Mishra",20,412,"English")
Mishra.show()

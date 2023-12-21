# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Person : 
    def __init__(self,name,age) :
        self.name = name 
        self.age = age

    @classmethod 
    def frm_str(cls,info) :
        name,age = info.split(",") 
        return cls(name , age)
        
person = Person.frm_str("Shardendu Mishra,19")
print(f"The name is {person.name} and the age is {person.age}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

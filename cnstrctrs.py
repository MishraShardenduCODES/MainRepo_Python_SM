# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# class Detail:
#     def __init__(self, anml, grp):
#         self.anml = anml
#         self.grp = grp
#     def info_zoo(self):
#         print(f"{self.anml} belongs to the {self.grp} group")
# str1 = input('Tell Animal name: ')
# str2 = input('Tell which group: ')
# a = Detail(str1, str2)
# a.info_zoo()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Person:
   def __init__(self):
        print("Hey I am a person")
   def info(self):  # gets called only when a.info() is called #
        print("Hi!!!!")

a = Person() # __init__ always gets called no matter what #
b = Person() # same always gets cancelled #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                    THIS IS THE MAIN FUNCTION                                                  #
class detail :
    def __init__(self, name1, age1, branch1) :
        self.name1 = name1
        self.age1 = age1
        self.branch1 = branch1
    def info(self):
        print(f'Hi {self.name1} you are {self.age1} y/o and your branch is {self.branch1}')

a = detail("Shardedndu Mishra",19,'CSE')
a.info()
b = detail("Anas Khan",1,'ECE')
b.info()
#                    THIS IS THE MAIN FUNCTION                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Student:
#     def __init__(self, age, name):
#         self.age = age  # public variable
#         self.name = name  # public variable

#     def show(self):
#         print(f"Name is {self.name} and age is {self.age}")

# obj = Student(21,"Harry")
# obj.show()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Student2:
#     def __init__(self, age, name):
#         self.__age = age               # private variable
#         self.__name = name             # private variable

# obj = Student2(21, "Harry")

# # Accessing private variables using name mangling
# print(obj._Student2__age)   # Accessing __age using the mangled name
# print(obj._Student2__name)  # Accessing __name using the mangled name
# print(__dir__())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"

# my_object = MyClass()

# print(my_object._nonmangled_attribute)       # Output: I am a nonmangled attribute
# # print(my_object.__mangled_attribute)         # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())
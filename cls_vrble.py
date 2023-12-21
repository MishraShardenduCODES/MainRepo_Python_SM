# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Employee :
    name = "Shardendu"
    age = 19
    cmp = "Tesla"
    nm_emp = 0
    def __init__(self) :
        
        Employee.nm_emp += 1
    def show(self) :
        print(f"Hi {self.name} you're age is {self.age} , as of now u work for {self.cmp} and ur company has {self.nm_emp} employee's.")

emp1 = Employee()
emp1.show()

emp2 = Employee()
emp2.name = "Shardendu Mishra"
emp2.cmp = "Apple"
emp2.age = 20
emp2.show()

# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Employee :
#     name = "Shardendu" # if name is already in init then u can't aassign it as a class variable #
#     age = 19           # same as name if age is a class variable tehn u cant assign it in init #
#     cmp = "Tesla"      # this is fine as cmp is a class varaible and can be used now #
#     nm_emp = 0         # initially the no of employee will be 0 #
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
#         Employee.nm_emp += 1  # as the user gives more input the no of employee will increase #
#     def show(self) :
#         print(f"Hi {self.name} you're age is {self.age} , as of now u work for {self.cmp} and ur company has {self.nm_emp} employee's.")
# emp1 = Employee()

# # # # # # # # # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
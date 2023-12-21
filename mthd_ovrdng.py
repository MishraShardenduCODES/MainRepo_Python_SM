class Area :
    def __init__ (self , num1 , num2) :
        self.num1 = num1 
        self.num2 = num2
    def area(self) :
        return (f"The area of rectangle is {self.num1*self.num2}")

class Area_cirlce(Area) : 
    def __init__(self , rad) : # U CANT NOT PASS TWO SAME PARAMETERS IN __init__ # 
        self.rad = rad
        super().__init__(rad,rad) 
    def area(self) :
        return (f"The area of circle is {3.141529*(self.rad**2):.4}")

rect = Area(5,4)
print(f"The area of rectangle is : {rect.area()}")

circle = Area_cirlce(3)
print(f"The area of circle is : {circle.area()}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THIS CODE WILL PRINT THE ANSWER TOO BUT IT WILL ALSO PRINT NONE #
# THIS IS BECAUSE THIS CODE RETRUNS NOTHING IN LINE 29 AND LINE 35 #
# class Area :
#     def __init__ (self , num1 , num2) :
#         self.num1 = num1 
#         self.num2 = num2
#     def area(self) :
#         print(f"The area of rectangle is {self.num1*self.num2}")
# class Area_cirlce(Area) : 
#     def __init__(self , rad) : # U CANT NOT PASS TWO SAME PARAMETERS IN __init__ # 
#         self.rad = rad
#         super().__init__(rad,rad) 
#     def area(self) :
#         print (f"The area of circle is {3.141529*(self.rad**2):.4}")
# rect = Area(5,4)
# print(f"The area of rectangle is : {rect.area()}")
# circle = Area_cirlce(3)
# print(f"The area of circle is : {circle.area()}")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# THIS CODE HAS ERROR IN LINE 11 AND I WROTE THIS CODE INITIALLY #
# THIS IS BECAUSE I HAVENT MADE Area AS THE PARENT CLASS IN Area_circle #
#
# class Area :
#     def __init__ (self , num1 , num2) :
#         self.num1 = num1 
#         self.num2 = num2
#     def area(self) :
#         print(f"The area of rectangle is {self.num1*self.num2}")
# class Area_cirlce : 
#     def __init__(self , rad) : # U CANT NOT PASS TWO SAME PARAMETERS IN __init__ # 
#         self.rad = rad
#         super().__init__(num1,num2) 
#     def area(self) :
#         print (f"The area of circle is {3.141529*(self.rad**2):.4}")
# rect = Area(5,4)
# print(f"The aera of rectangle is : {rect.area()}")
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
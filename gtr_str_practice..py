
class student : 
    def __init__(self,name,mark,age,grade) :
        self.name = name 
        self.mark = mark
        self.age = age
        self.grade = grade 
    
    # MAKING UP A GETTER #
    @property
    def student_info(self) : # HERE WE DONT HAVE TO PASS ONLY SELF AS AN ARGUMENT #
        return(f"Hi!! {self.name}, you have got {self.mark} marks ,you are {self.age} y/o and you are in grade {self.grade}")
    
    # SETTING UP A SETTER #
    @student_info.setter
    def student_info(self,new_info) :
        name, mark, age, grade = new_info.split(',')
        self.name = name 
        self.mark = int(mark)
        self.age = int(age)
        self.grade = float(grade)

obj = student('Shardendu Mishra',97,19,12)
print(obj.student_info)

obj.student_info = 'John Doe, 85, 20, 11'
print(obj.student_info)

# USING SPLIT WAS NOT NECESSARY BUT THEN U WILL HAVE TO PASS FUNCTIONS LIKE IN LINE 23-24 #
# IF U DONT HAVE ANY NEW CHANGE TO MAKE IN SETTER TEHN JUST SIMPLY WRITE :
# name, mark, age, grade = new_info
# self.name = name 
# self.mark = int(mark)
# self.age = int(age)
# self.grade = float(grade)

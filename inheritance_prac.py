# THIS PROGRAM EXPALINS HOW INHERITANCE WORKS #
# STUDENT IS A PARENT CLASS AND PROGRAM IS A CHILD CLASS #

class Student :
    def __init__ (self,name,section) :
        self.name = name 
        self.section = section
    
    def info_std(self) :
        print(f'The student named {self.name} is in section {self.section.upper()}')
    
class Good_students(Student) :
    def info_good_std(self):
        print(f'{self.name} is a star student in section {self.section.upper()}')

s1 = Student('Shardendu Mishra','b')
s1.info_std()
print('\n\n')
s2 = Good_students('Meghana Mishra','a')
s2.info_std()
s2.info_good_std()
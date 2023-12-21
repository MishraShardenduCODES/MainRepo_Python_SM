class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Person(Human):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def show(self):
        super().show()
        print("Address:", self.address)

class Student(Person):
    def __init__(self, name, age, address, program):
        super().__init__(name, age, address)
        self.program = program

    def show(self):
        super().show()
        self.program.show()

class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)

s = Student("Shardendu Mishra", 20, "11/363 Souter Ganj Kanpur", Program("CSE", "4 years"))
s.show()

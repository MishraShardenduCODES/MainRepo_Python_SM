class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Name:", self.name)

class Dog(Animal):
    
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed
    
    def show(self):
        Animal.show(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color
    
    def show(self):
        Animal.show(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Tuffy","GS")
dog.show()

cat = Cat("Mna","Orange")
cat.show()
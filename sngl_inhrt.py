# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Animal :
    def __init__(self,name,species) :
        self.name = name 
        self.species = species 
    def make_sound1(self) :
        print(f"A {self.name} make this sound :")

class Cats(Animal) :
    def __init__(self,name,breed) :
        self.breed = breed 
        super().__init__(name,"Orange")
    def make_sound(self) :
        print("Meow!")

cat = Cats("Cat","Orange")
cat.make_sound1()
cat.make_sound()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
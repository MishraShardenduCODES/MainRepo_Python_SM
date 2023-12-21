class Grandfather:
    def __init__(self, nameg, gnrtn):
        self.nameg = nameg
        self.gnrtn = gnrtn

    def show1(self):
        print(f"{self.nameg} is your Name and you are the {self.gnrtn} Generation of your family")

class Father(Grandfather):
    def __init__(self, namep, gnrtn2, nameg):
        self.namep = namep
        self.gnrtn2 = gnrtn2
        # Pass both nameg and gnrtn2 to the Grandfather's __init__ method
        super().__init__(nameg, gnrtn2)

    def show2(self):
        print(f"{self.namep} is your name and you are the {self.gnrtn2} Generation of your family. {self.nameg} is your Father")

class Child(Father):
    def __init__(self, name, gnrtn, namep, nameg):
        self.name = name
        self.gnrtn = gnrtn
        super().__init__(namep, gnrtn, nameg)

    def show3(self):
        print(f"{self.nameg} is your GrandPa. "
              f"{self.namep} is your Father. "
              f"{self.name} is your name and you are the {self.gnrtn} Generation of your family")


gf = Grandfather("A Mishra", "1st")
gf.show1()
print("\n\n")

pa = Father("B Mishra", "2nd", "A Mishra")
pa.show1()
pa.show2()
print("\n\n")

kd = Child("C Mishra", "3rd", "B Mishra", "A Mishra")
kd.show1()
kd.show2()
kd.show3()
print("\n\n")

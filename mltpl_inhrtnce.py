# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Employee :
    def __init__(self,name) :
        self.name = name
    def show1(self) :
        print(f"You're name is : {self.name}")
class Dancer :
    def __init__(self,dnc_typ) :
        self.dnc_typ = dnc_typ
    def show2(self) :
        print(f"You do {self.dnc_typ}")
class dncr_emplye(Employee,Dancer) :
    def __init__(self,name,dnc_typ) :
        Employee.__init__(self,name)
        Dancer.__init__(self,dnc_typ)
    def show3(self) :
        print(f"HI {self.name}!! You do {self.dnc_typ}.")
a1 = Employee("Mna Mishra")
a1.show1()
a2 = Dancer("Kathak")
a2.show2()
a3 = dncr_emplye("Mna Mishra","Kathak")
a3.show3()
print(dncr_emplye.mro())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


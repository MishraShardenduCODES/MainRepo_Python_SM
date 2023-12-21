class Vector :
    def __init__ (self,i,j,k) :
        self.i = i
        self.j = j
        self.k = k
    def __add__(self,n) :
        return Vector(self.i + n.i,self.j + n.j,self.k + n.k)
    def __sub__(self,n) :
        return Vector(self.i - n.i,self.j - n.j,self.k - n.k)

    def __str__(self) :
        return f"{self.i}.i + {self.j}.j + {self.k}.k"

v1 = Vector(3,5,6)
print(f"First Vector is : {v1}")

v2 = Vector(1,9,5)
print(f"First Vector is : {v2}")

print("\n")
print(f"The sum of the vectors is : {v1 + v2}")
print(type(v1 + v2))

print("\n")
print(f"The difference of the vectors is : {v1 - v2}")
print(type(v1 - v2))
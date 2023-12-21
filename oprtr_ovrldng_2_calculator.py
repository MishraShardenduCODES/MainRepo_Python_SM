class arth_opr:
    def __init__(self, num1):
        self.num1 = num1            
    def __add__(self, n):
        return arth_opr(self.num1 + n.num1)
    def __sub__(self, n):
        return arth_opr(self.num1 - n.num1)
    def __mul__(self, n):
        return arth_opr(self.num1 * n.num1)
    def __truediv__(self, n):
        return arth_opr(self.num1 / n.num1)
    def __lt__(self, n):
        return self.num1 < n.num1
    def __gt__(self, n):
        return self.num1 > n.num1
    def __eq__(self, n):
        return self.num1 == n.num1
    
n1 = arth_opr(5) 
print(f"The number is : {n1.num1}")

n2 = arth_opr(8) 
print(f"The number is : {n2.num1}")

print(f"The sum of the numbers is : {(n1 + n2).num1}")
print(f"The diff of the numbers is : {(n1 - n2).num1}")
print(f"The prd of the numbers is : {(n1 * n2).num1}")
print(f"The div of the numbers is : {(n1 / n2).num1}")
print(f"Is {n1.num1} smaller than {n2.num1} ? : {n1 < n2}")
print(f"Is {n1.num1} greater than {n2.num1} ? : {n1 > n2}")
print(f"Are the two numbers equal ? : {n1 == n2}")
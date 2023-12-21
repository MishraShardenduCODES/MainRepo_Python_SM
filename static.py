class Math : 
    def __init__(self,num1,num2): 
        self.num1 = num1
        self.num2 = num2
    
    def add_num(self):
        return self.num1 + self.num2

    def show(self):
        add = self.add_num()
        print(f"The sum is = {add}")
    
    @staticmethod 
    def add(a,b):
        print(f"The sum is = {a + b}")
    
mat1 = Math.add(5,5)

mat2 = Math(4,6)
mat2.show()
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class MyClass:
  def __init__(self, value):
      self.value = value
    
  @property # getter #
  def ten_value(self): 
      return 10*self.value
    
  @ten_value.setter # make it a setter #
  def ten_value(self, new_value):
      self.value = new_value/100

obj = MyClass(1)
obj.ten_value = 67 # wont work until we dont use setter #
print(obj.ten_value)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

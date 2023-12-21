# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Coordinates: ({self.x}, {self.y})'
    def __str__(self):
        return f'Coordinates: ({self.x}, {self.y})'

obj = MyClass(3, 4)

print(str(obj))   # Output using __str__
print(repr(obj))  # Output using __repr__

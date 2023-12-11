# Example of SyntaxError
x = int(input("Tell a value : "))
if x == 5:  # Added colon at the end of the line
    print("x is 5")

# Example of IndentationError
for i in range(5):
    print(i)  # Added indentation for the print statement

# Example of NameError
some_variable = 42  # Defined 'some_variable'
print(some_variable)

# Example of TypeError
result = "5" + str(6)  # Converted the integer to a string before adding

# Example of IndexError
my_list = [1, 2, 3]
# Index 3 does not exist in 'my_list', changed to a valid index
print(my_list[2])

# Example of ValueError
try:
    num = int("42")  # Converted a valid numeric string to an integer
except ValueError as e:
    print(f"ValueError: {e}")

# Example of KeyError
my_dict = {'a': 1, 'b': 2}
# Key 'c' does not exist in 'my_dict', changed to an existing key
print(my_dict['a'])

# Example of ZeroDivisionError
try:
    result = 10 / 2  # Divided by a non-zero number
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# AttributeError Example
class MyClass:
    def __init__(self, value):
        self.value = value
my_instance = MyClass(42)
try:
    print(my_instance.value_not_exist)  # Accessed an existing attribute 'value'
except AttributeError as e:
    print(f"AttributeError: {e}")

# FileNotFoundError Example
try:
    with open('existing_file.txt', 'r') as file:  # Created a file 'existing_file.txt'
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

a = "!!!!!!!!!!!!!!!I am Shardendu Mishra I am From Kanpur UP!!!!!!!!!!!!!" 

print("1st : ",a.strip("!"))
b=a.strip("!")

c = "IamMishra980"

print("2nd : ",a.rstrip("!"))

print("3rd : ",a.lstrip("!"))

print("4th : ",b.upper())

print("5th : ",b.lower())

print("6th : ",b.capitalize())

print("7th : ",b.find("am"))

print("8th : ",b.split())

print("9th : ",b.replace("am","still am"))

print("10th : ",b.endswith("UP"))

print("11th : ",b.center(10))

print("12th : ",c.isalnum())

print("13th : ",c.isalpha())

d = "\n"
print("14th : ",d.isprintable())

e = "    ded  "
print("15th : ",e.isspace())

print("16th : ",b.isupper())

f = "I am Shardendu Mishra"
print("17th : ",f.startswith("I am"))

print("18th : ",f.swapcase())

g="i am from kanpur!! how are you ?"
print("19th : ",g.title())
a10 = -8
print(abs(a10))


a11 = [ 1 , 2 , 4 , 3 ] 
b11 = iter(a11)
for i in range(4) :
    print(next(b11))

a1 = [ True , True , False ]
a2 = ( 10 , 20 , 30 , 0 )
a3 = { 'a' : 10 , 'b' : 20 , 'c' : 30 }

print(all(a1))
print(all(a2))
print(all(a3))

print("\n")

print(any(a1))
print(any(a2))
print(any(a3))

name = "Shardendu Mishra"
print(ascii(name))

print(bin(100))
print(bool(1))
print(bool(0))

print(complex(4,5))
print(pow(2,4))

lst = [ 1 , 5 , 7 , 2 , 9 ]
print(max(lst))
print(min(lst))
print(sum(lst))

a = [ 1 , 3 , 5 , 6 ]

print(1 in a)
print(9 not in a)

b = 'Hi Everyone I am Shardendu Mishra'
print(b.casefold())

c = 'Hi\tBro'
print(c.expandtabs(tabsize = 1))
print(c.expandtabs(tabsize = 2))
print(c.expandtabs(tabsize = 8))
print(c.expandtabs(tabsize = 16))

d = ' Shardendu Mishra '
e = 19
f = 98.456789
print("Hi!! , {} how are you ? You are {} y/o and u got {:.2f}% marks ".format( d , e , f))
print("Hi!! , {} how are you ? You are {} y/o and u got {:.0f}% marks ".format( d , e , f))

#alternate of format 
print(f"Hi!! , {d:} how are you ? You are {e:} y/o and u got {f :.2f}% marks ")
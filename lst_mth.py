l1 = [i for i in range ( 1 , 11 , 2 ) ]
print(l1)
l2 = [i for i in range ( 0 , 11 , 2 ) ] 
print(l2)

l3 = [5 , 4 , 8 , 9 , 1 , 0]
lm = l3.copy()

l3.sort()
print(l3)

l3.append(4)
print(l3)

l3.insert(0,1)
print(l3)

l3.pop(1) #index 1
print(l3)

l3.remove(4) 
print(l3)

print(l3.count(1))
print(l3.index(5))
print(lm)
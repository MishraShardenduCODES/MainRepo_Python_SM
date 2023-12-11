s = {2,2,3,5,6,8,9,1,2,4}
print(s)
# unordered immutable and  dont use duplicate elements

name = {} # This is a dictionary #
names = set() # This is a set #

print(type(name))
print(type(names))

a5 = {1,2,3,4,5}
b5 = {6,7,8,9,10}

# union and update 
c5 = a5.union(b5)
b5.update(a5)
print(b5)
print(c5)

# intersection and intersectio_update
a4 = {5,3,8,0,9,2}
b4 = {1,3,7,3,9,4}
c4 = a4.intersection(b4)
b4.intersection_update(a4)

print(b4)
print(c4)

# symmetric_difference() and symmeteric_difference_update()
a3 = {5,3,8,0,9,2}
b3 = {1,3,7,3,9,4}
c3 = a3.symmetric_difference(b3)
b3.symmetric_difference_update(a3)

print(b3)
print(c3)  

# difference() and difference_update()
a2 = {1,2,3,4}
b2 = {2,3,6,5}
c2 = a2.difference(b2)
b2.difference_update(a2)

print(b2)
print(c2)

# disjoint subset superset
a = {1,2}
b = {3,4}
e = {1,2,3,4,5,6}
f = {3,4,5}

c = a.isdisjoint(b)
g = f.issubset(e)
h = e.issuperset(f)

print(c)
print(g)
print(h)


s1 = {2,1,5,4,3}
s1.add(9)
print(s1)

s2 = {10,11,12,14}
s1.update(s2)
print(s1)

s1.remove(14)
print(s1)

s3 = {4,2,1,8}
items = s3.pop()
print(s3)
print(items)

s4 = {4,2,1,5}
s4.clear()
print(s4)

s5 = {1,3,5,7,9,10}
del s5
# print(s5) -> This will retrun error if executed 
# this is because s5 no longer exists

st = {''}
st2 = {}

print(type(st))
print(type(st2))
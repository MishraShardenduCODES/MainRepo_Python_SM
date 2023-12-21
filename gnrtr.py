def mgtr():
    for i in range(5):
        yield i
gen = mgtr()
print(next(gen))
print("Hi")
print(next(gen))

# # # # # # # # # # # # # # # # # # # # # # # # 

def mgtr():
    for i in range(5):
        yield i
gen = mgtr()
for i in gen :
    print(i)
with open('random.txt','w') as p3 :
    p3.write("Hello Bhai")
    p3.truncate(5)

with open('Poem.txt','r+') as p :
    p.seek(10)
    data = p.read(5)
    a = p.tell()
    print(data)
    print(a)

# WRITTING A FILE #
f = open('Hello.txt','w')
f.write("Hi There !!")
f.close()

# WRITTING A FILE USING WITH #
with open('Hello2.txt','a') as f:
    f.write("Hi There !!")


# READING A FILE #
with open('Hello.txt','r') as o:
    text = o.read()
    print(text)
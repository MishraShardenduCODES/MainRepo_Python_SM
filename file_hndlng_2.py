poem = 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested. \nSparse is better than dense. \nReadability counts.\nSpecial cases arent special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless youre Dutch. \nNow is better than never. \nAlthough never is often better than *right* now. \nIf the implementation is hard to explain, its a bad idea. \nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- lets do more of those!'


# WRITTING USING WRITE #
with open('Poem1.txt','w') as p1 :
    p1.write(poem)
    p1.write("Done!!!!")


# WRITTING USING WRITE #
with open('Poem2.txt','w') as p2 :
    lst = list(poem)
    p2.writelines(lst)

# reading already existing file #
with open('Poem.txt','r') as p :
    while True :
        line = p.readline()
        if not line : 
            break
        print(line)


# THIS IS TO READ A FILE USING READLINE #
with open('Poem1.txt','r') as p :
    while True :
        line = p.readline()
        if not line : 
            break
        print(line)


# THIS IS TO READ A FILE USING READLINES #
with open('Poem2.txt', 'r') as p2:
    line = p2.readline()
    while line:
        print(line.strip())  # Strip to remove extra newline characters
        line = p2.readline()
tpl = ( 'Hi' , '!!!' , 'I' , 'am' , 'Shardendu' , 'Mishra' , '!!!!!' )
print(tpl)

lst = list(tpl)
lst.append('I am from Kanpur.')
lst.pop(5)
lst[0] = 'Hello'
tpl = tuple(lst)
print(tpl)

string = " ".join(str(i) for i in tpl)
print(string)
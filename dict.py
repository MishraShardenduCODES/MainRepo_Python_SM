dict = { 'Name' : 'Shardendu Mishra' , 'Age' : 19 , 'Eligible' : 'Yes' }
print(dict.values())
print(dict.keys())
print(dict.items())

dict.update( {'school' : 'D.P.S Kalyanpur '})
print(dict)

dict2 = { 'Name' : 'Shardendu Mishra' , 'Age' : 19 , 'Eligible' : 'Yes' }
dict2.clear()
print(dict2)

dict.pop( 'Age' )
print(dict)

dict.popitem()
print(dict)

del dict2
# print( dict2 ) -> This will retrun error if executed 
# this is because dict2 no longer exists

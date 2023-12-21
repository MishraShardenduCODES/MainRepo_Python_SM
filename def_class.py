class person :
    name = 'Shardednu MIshra'
    age = 19
    networth = 10000
    def info(self) :
        print(f"Hi!!!! {self.name} , how are you ?, Your networth is ${self.networth} and you're just {self.age} y/o") 

# # # # # # # # # # # # # # # # # # 
obj = person()
obj.info()
# # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # 
a = person()
a.name = str(input("Tell name : "))
a.networth = int(input("Tell your networth : "))
a.age = int(input("Tell age : "))
a.info()


# # # # # # # # # # # # # # # # # # 
b = person()
b.name = str(input("Tell name : "))
b.networth = int(input("Tell your networth : "))
b.age = int(input("Tell age : "))
b.info()
import time 
print(time.time())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("Hi!!!!")
time.sleep(5)
print("Bye!!!")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

def func1():
  try:
    l = [12, 45, 56, 17]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  finally:
    print("I am always executed")

x = func1()
print(x)
 # Finally is always executed even if function is returned #
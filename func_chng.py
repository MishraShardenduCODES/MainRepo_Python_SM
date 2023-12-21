# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import functools

@functools.lru_cache(maxsize = None) 
def fib(n) :
    if n < 2 :
        return n
    else :
        return fib(n-2)+fib(n-1)
    
print(fib(200))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import functools
import time

@functools.lru_cache(maxsize = None)
def fx(n):
  time.sleep(5)
  return n*5
    
# HERE SLEEP IS NOT NECESSARY IT IS JUST FOR REPRESENTATION #
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")
# Output: 6765

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
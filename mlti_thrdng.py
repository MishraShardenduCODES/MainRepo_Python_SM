# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# IF .join() IS USED THEN ALL WILL BE EXECUTED WHEN THE SLOWEST STEP IS COMPLETED #
# IF .join() IS NOT USED THEN IT WILL BE EXECUTED IN LESS THAN A SEC VERY QUICKLY #

import threading
import time

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return sec

def main():
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    time1 = time.perf_counter()
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2 - time1)

main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
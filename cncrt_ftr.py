# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from concurrent.futures import Executor, ThreadPoolExecutor
import time
import threading
import time

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return sec

# def main():
    # t1 = threading.Thread(target=func, args=[4])
    # t2 = threading.Thread(target=func, args=[2])
    # t3 = threading.Thread(target=func, args=[1])

    # time1 = time.perf_counter()
    # t1.start()
    # t2.start()
    # t3.start()

    # t1.join()
    # t2.join()
    # t3.join()

    # time2 = time.perf_counter()
    # print(time2 - time1)

# main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def poolingDemo() :
    with ThreadPoolExecutor( ) as executer :
        f1 = executer.submit(func,5)
        f2 = executer.submit(func,3)
        f3 = executer.submit(func,1)

        print(f1.result())
        print(f2.result())
        print(f3.result())

        # l = [ 3 , 5 , 1 , 2 ]
        # results = Executor.map(func,l)
        # for results in results :
        #     print(results)

        # map is another syntax to execute it #
    
poolingDemo()    
# if f1 f2 f3 are used then the time for execution is 5 sec #
# this is as first all will be executed then the output will be given according to there time #
# if we use same variable such as f then it will be done in 1 sec #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
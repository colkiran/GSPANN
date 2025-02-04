
import time

def timeCalc(fnc):

    def helper(x):
        print("Executing the function.....")
        st = time.perf_counter()
        fnc(x)
        et = time.perf_counter()
        print("Completed executing the function.....")
        print(f"The total time taken by the function to execute :{round(et - st, 2)}")

    return helper


@timeCalc
def fun(x):
    lst = []
    for i in range(x):
        for j in range(1, i + 1):
            lst.append(i ** 3)


fun(6500)

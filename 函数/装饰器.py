import time
import functools


def time_it(func):
    # 使用 内置装饰器 wraps 能让__name__ 始终指向源函数
    @functools.wraps(func)
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"func函数的执行时间是:{end - start}s")

    return wrapper


@time_it
def work_fna():
    print("函数开始执行")
    time.sleep(1)
    print("函数执行结束")


# work_fna()
#
# print(work_fna.__name__)


# 练习

def exec_fnc(fnc):
    @functools.wraps(fnc)
    def wrapper(num=1):
        for i in range(num):
            start = time.time()
            fnc()
            end = time.time()
            print(f"{fnc.__name__}函数第{i + 1}执行的时间是:{end - start}")

    return wrapper


@exec_fnc
def demo_fnc():
    print("函数执行了")
    time.sleep(1)
    print("函数执行结束了")


demo_fnc(2)

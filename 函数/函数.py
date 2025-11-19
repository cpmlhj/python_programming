# def foo():
#     print('foo')
#     print('function')
#
#
# foo()
#
# # 匿名函数 使用lambda 表达式
#
# add1 = lambda x: x + 1
#
#
# def add2(x):
#     return x + 1
#
# # add1 == add2


# def foo1(n1: int, n2: int) -> int:
#     return n1 * n2
#
#
# def foo3(arg1, argv2, argv3):
#     print(arg1)
#     print(argv2)
#     print(argv3)
#
#
# foo3('one', 'two', 'three')
# # 关键字参数
# foo3(arg1='one', argv3='three', argv2='two')

# for i in range(10):
#     # print(((-1) ** i) / i * 2 + 1)
#     print((-1) ** i)
#     print(i * 2 + 1)

# * 接收位置参数  **接收关键字参数
def address(name, *tel, alias_name, **custom):
    """
    函数用来表示 函数参数的高级用法
    :param name:
    :param tel:
    :param alias_name:
    :param custom:
    :return:
    """
    print(f"name:{name}, tel:{tel}, alias:{alias_name}, cust:{custom}")


address('cpm', 'asd', 'a134123', 'aerwqer', alias_name='3123', custom={"one": 1, "two": 2})
# 函数内省属性 函数注释文档
print(address.__doc__)

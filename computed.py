# 实现一个简易的计算器

num1 = input("输入第一个数字")
num2 = input("请输入第二个数字")
op = input("输入运算符号")
# print(num1)

result = eval(f"{num1} {op} {num2}")
print(result)

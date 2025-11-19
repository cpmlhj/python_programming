# 列表 list
#
# list_demo = ['a', 'b', 'c', 'd', 'e', ['f', 'g']]
#
# print(type(list_demo))
#
# # 对原始列表做修改
# list_demo.insert(0, 'first')
#
# list_demo.insert(-1, 'last')
#
# list_demo.append('real_last')
#
# list_demo.extend("last")
#
# print(list_demo)
#
# # remove pop
#
# # remove 的参数是元素值, pop 是索引
# list_demo.remove("real_last")
#
# pop_result = list_demo.pop(0)
#
# print(f"list is {list_demo}")
# print(pop_result)
# print(list_demo.count("a"))
#
# # 练习
# # 列表中重复的元素 ‘c’ 移除
#
# list_pc = ['a', 1, 'b', 2, 'c', 'c', 3]
# list_pc.remove('c')
# print(list_pc)

# 元组
# tup_demo = tuple(["x", "y", "z"])
#
# # print(tup_demo[3])  # tuple index out of range
#
# del tup_demo[3]  # tuple object doesn't support item deletion


# ---------- 集合 ----------

color = ('r', 'g', 'b', 'a', 'a', 'b', 'c')
set_color = set(color)
print(tuple(set_color))

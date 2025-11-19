# 条件语句

# if False:
#     print("done")
# # else:
# #     print("不成立")
# elif True:
#     print("你看看")

import random

num = int(random.random() * 100 + 1)

if num % 3 == 0:
    print(num)
else:
    print("不成立")

# match 语句

# match num:
#     case 400:
#         print(400)
#     case 500 | 501 | 502:
#         print("模式组合")
#     case _:
#         print('default')

# 循环语句
#
# while_num = 4
# while while_num > 0:
#     print(while_num)
#     # case_num = while_num - 1
#     # while_num = case_num
#     while_num -= 1
# import random
#
# random_num = int(random.random() * 100 + 1)
#
# input_num = input("请输入您的答案")
# count = 3
#
# while count > 0:
#     if int(input_num) == random_num:
#         print(f"你的输入正确啦 {input_num} --- 随机数是{random_num}")
#         break
#     count -= 1
#     if count == 0:
#         print(f"正确的答案是{random_num}")
#         break;
#     input_num = input("请输入您的答案")


#  for循环

movie = {"name": "Friends", "language": "en", "sessions": 10, "Other": "Six of hit"}

# for title, value in movie.items():
#     print(title)
#     print(value)

# for i in enumerate(movie.items()):
#     print(i)


# list = [i for i in (1, 2, 3, 4)]

# list2 = [i*i for i in (1,2,3,4)]

# list3 = [i * i for i in (1, 2, 3, 4) if i < 2]


# 练习
demo_list = ["rachel", "monica", "phoebe", "joey"]
demo_list.sort()

demo_list = [(i[0], i[1].capitalize()) for i in enumerate(demo_list)]
print(demo_list)

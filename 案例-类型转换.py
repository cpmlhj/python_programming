import pprint

# with open('./demo.txt') as file:
#     file_data = file.readlines()
#     # pprint.pprint(file_data)
#     # 输出文章行数
#     print(len(file_data))
#     # 输出文章空行
#     print(file_data.count('\n'))
#     # 输出非空行数
#     print(len(file_data) - file_data.count('\n'))
#     print(len(set(file_data)) - 1)
#     # 统计rem出现的次数
#     print(str(file_data).split(" ").count("you"))


#
with open('./demo.csv') as file:
    file_data = file.readlines()
    file_data.pop(0)
# print(file_data)

from tinydb import TinyDB
from tinydb import Query

db = TinyDB('./db.json')
friend = Query()
# db_list = []
# for x in file_data:
#     friend_arr = x.split(",")
#     db_list.append({
#         "id": friend_arr[0],
#         "name": friend_arr[1],
#         "source": friend_arr[2],
#         "mobile": friend_arr[3]
#     })
#
# db.insert_multiple(db_list)
friend_info = db.search(friend.name == '张三')
print(friend_info)

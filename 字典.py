# 定义一个新的字典

dict_demo = {"one": 1, "two": 2}

dict_demo2 = dict(one=1, two=2)

dict_demo3 = {x: x ** 2 for x in range(10)}

print("x" in dict_demo)

# 遍历字典
# print(dict_demo.items())
# print(dict_demo.values())
# print(dict_demo.keys())
# print(dict_demo.get('one'))

for key, value in dict_demo.items():
    print(key)
    print(value)

# # 操作字典元素
# print(dict_demo.pop("one"))
# # popitem 移除字典最后一个元素
# print(dict_demo.popitem())

one_default = dict_demo.setdefault("one2")
print(one_default)
print(dict_demo)

# 练习

phone_dict = {
    "liuhaojun": {
        "desc": None,
        "email": "345829331@qq.com",
        "phone": list([x for x in range(2)])
    },
    "cpm": {
        "desc": None,
        "email": "345829330@qq.com",
        "phone": list([x for x in range(2)])
    },
}

phone_dict.setdefault("dda", {
    "desc": "ddas",
    "email": "33@qq.com",
    "phone": ["123", "4312"]
})

print(phone_dict)
print(phone_dict.popitem())

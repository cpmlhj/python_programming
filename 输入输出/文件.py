import os

# mode 参数 r=读取、w=覆盖写入、 a=追加写入，如果文件存在则在末尾添加
# b=二进制模式
# F = open('./demo.txt', mode="w", encoding="GBK")
#
# F.write("人生苦短")
# F.close()

# F = open('./demo.txt', mode='r', encoding="GBK")
# data = F.readlines()
# print(data)


# F = open('./demo.txt', mode='r', encoding='GBK')
#
# # data = F.read(2)
#
# for data in F:
#     print(data)
#
# F.close()

# 使用with 语法可以不手动执行 close with执行完后会自动关闭
with open('./demo.txt', mode='r', encoding='GBK') as File:
    data = File.read(2)
    print(data)

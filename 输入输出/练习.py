# 合并文件

with open("./text1.txt") as File1:
    file_data1 = File1.read()

with open("./text2.txt") as File2:
    file_data2 = File2.read()

with open("./text3.txt", mode='w') as File3:
    File3.write(file_data1)
    File3.write(file_data2)

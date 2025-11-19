import argparse

# 执行方式 python3 argparse_demo.py -number 100

parse = argparse.ArgumentParser(description="这个程序用来演示参数处理")

parse.add_argument("-number", help="请输入一个数字")

# 强制转换参数类型和默认值
parse.add_argument("- number1", type=int, default=9)

args = parse.parse_args()

print(f"你输入的参数是{args.number}")

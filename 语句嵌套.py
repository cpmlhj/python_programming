# for x in range(1, 10):
#     for j in range(1, x + 1):
#         print(f"{x} * {j} = {x * j}")
import random

### 飞机大战

from pynput.keyboard import Key, Listener, KeyCode

plane_data = [
    [0, 0, 0],
    [0, "x", 0],
    [0, 0, 0]
]

plane_idx = []
plane_num = 100

for i in enumerate(plane_data):
    print(i[1])
    try:
        targetPlane = i[1].index("x")
        plane_idx = [i[0], targetPlane]
    except ValueError:
        continue


def on_press(key):
    next_idx = []
    global plane_num
    if KeyCode.from_char("w") == key:
        if plane_idx[0] != 0:
            next_idx = [plane_idx[0] - 1, plane_idx[1]]
    elif KeyCode.from_char("s") == key:
        if plane_idx[0] < len(plane_data) - 1:
            next_idx = [plane_idx[0] + 1, plane_idx[1]]
    elif KeyCode.from_char("a") == key:
        if plane_idx[1] != 0:
            next_idx = [plane_idx[0], plane_idx[1] - 1]
    elif KeyCode.from_char("d") == key:
        if plane_idx[1] < len(plane_data[plane_idx[1]]) - 1:
            next_idx = [plane_idx[0], plane_idx[1] + 1]
    elif KeyCode.from_char("+") == key:
        add_num = int(random.random() * 100 + 1)
        plane_num += add_num
        if plane_num > 100:
            plane_num = 100
    elif KeyCode.from_char('-') == key:
        cut_num = int(random.random() * 100 + 1)
        plane_num -= cut_num
        if plane_num < 0:
            print("游戏结束 你的血没了")
            exit(-1)
    else:
        return

    if len(next_idx) != 0:
        plane_data[plane_idx[0]][plane_idx[1]] = 0
        plane_data[next_idx[0]][next_idx[1]] = "x"
        plane_idx[0] = next_idx[0]
        plane_idx[1] = next_idx[1]
    for x in plane_data:
        print(x)
    print(plane_num)


with Listener(on_press=on_press) as listener:
    listener.join()

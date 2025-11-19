def foo():
    return 'ab'


def recor(num):
    if num == 1:
        return 1
    else:
        return num * recor(num - 1)


print(recor(19))

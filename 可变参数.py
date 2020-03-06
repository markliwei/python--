# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add(), end=' ')
print(add(1), end=' ')
print(add(1, 2), end=' ')
print(add(1, 2, 3), end=' ')
print(add(1, 3, 5, 7, 9), end=' ')

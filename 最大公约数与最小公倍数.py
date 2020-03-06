"""
Version: 0.1
Author: 范永杰
Date: 2019-09-30
"""


def gcd(x, y):
    """求最大公约数"""
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if (x % factor == 0)and(y % factor == 0):
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)



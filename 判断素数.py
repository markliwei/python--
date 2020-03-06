"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 范永杰
Date: 2019-09-29
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
print(is_prime)
print(is_prime and num)
if is_prime and num != 1:       #import random
                                #print(True and random.randint(-100, 100))
                                #output:random.randint(-100, 100)

    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

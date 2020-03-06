"""
水仙花数
"""
print('所有的水仙花数：')
for num in range(100, 1000):
    i = num % 10
    j = num // 10 % 10
    k = num // 100
    if num == i ** 3 + j ** 3 + k ** 3:
        print(num)
"""
正整数的反转
每次取出个位上的数字
"""
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

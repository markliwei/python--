"""
100求和

sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print(sum)


猜随机数

import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请猜一个数字：'))
    if answer > number:
        print('在大一点')
    elif answer < number:
        print('在小一点')
    else:
        print('恭喜你猜对了')
        break
print('你总共猜了%d次' % counter)
"""
for i in range(1, 10):      #循环从1到9
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')       #每输出空一个tab
    print()     #换行

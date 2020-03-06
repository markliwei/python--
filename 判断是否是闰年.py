"""
运算符优先级
算术大于位运算符大于比较大于！=大于逻辑大于赋值

闰年：能被400整除或者能被4整除但不能被100整除
"""
year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)


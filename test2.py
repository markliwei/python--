"""
使用input函数输入
使用int（）进行类型转换
用占位符格式化输出的字符
"""
a = int(input('a = '))
b = int(input('b = '))
print('%s + %s = %s' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%f * %f = %f' % (a, b, a * b))
print('%s / %s = %s' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%f %% %f = %f' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))


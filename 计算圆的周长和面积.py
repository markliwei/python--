import math

r = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * r
area = math.pi * r * r
print('周长：%.2f' % perimeter)
print('面积: %.2f' % area)

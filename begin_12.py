from math import *

a = int(input('Введите катет прямоугольного треугольника "а": '))
b = int(input('Введите катет прямоугольного треугольника "b": '))
c = sqrt(a * a + b * b)
p = a + b + c
print('Гипотенуза прямоугольного треугольника {} и {} равна {}'.format(a, b, c))
print('Периметр прямоугольного треугольника {} и {} равен {}'.format(a, b, p))
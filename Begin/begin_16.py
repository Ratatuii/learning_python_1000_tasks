# задание №16
# Найти расстояние между двумя точками с заданными координата-
# ми x1 и x2 на числовой оси: |x2 − x1 |.
from math import *
x1 = int(input())
x2 = int(input())
l = abs(x1 - x2)
print('Расстояние между двумя точками с заданными координатами x1 = {}, x2 = {} равно l = {}'.format(x1, x2, l))
# Задание №17
# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
# и BC и их сумму.
# from math import *

A = int(input())
B = int(input())
C = int(input())
AC = abs(A - C)
BC = abs(B - C)
summ = AC + BC
print(
    'На числовой оси A = {} B = {} C = {} произведение точек AC = {} и BC = {} равны {}'.format(A, B, C, AC, BC, summ))

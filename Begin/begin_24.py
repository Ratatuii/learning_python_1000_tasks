# Задание №24
# Даны переменные A, B, C. Изменить их значения, переместив содер-
# жимое A в C, C — в B, B — в A, и вывести новые значения переменных A,
# B, C.
a = int(input())
b = int(input())
c = int(input())
print('Введенные значения a = {} b = {} c = {}'.format(a, b, c))
print('Меняем местами содержимое b = a, c = b, a = c')
a, b, c = b, c, a
print('Получаем: a = {} и b = {} c = {}'.format(a, b, c))

# Задание №26
# Найти значение функции y = 4(x−3) 6 − 7(x−3) 3 + 2 при данном
# значении x.
x = int(input())
y = (4 * ((x - 3) ** 6) - (7 * ((x - 3) ** 3)) + 2)
print('Значение функции y при заданном значении x = {} будет равно = {} '.format(x, y))

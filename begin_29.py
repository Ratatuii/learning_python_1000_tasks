# Задание №28
# Дано число A. Вычислить A 15 , используя две вспомогательные пере-
# менные и пять операций умножения. Для этого последовательно находить
# A**2 , A**3 , A**5 , A**10 , A**15 . Вывести все найденные степени числа A.
a = int(input())
a2 = a * a
a3 = a2 * a
a5 = a2 * a3
a10 = a5 * a5
a15 = a10 * a5
print('Степени числа {0} ** 2 = {1}, {0} ** 3 = {2}, {0} ** 5 = {3}, {0} ** 10 = {4}, {0} ** 15 = {5}'.format(a, a2, a3,
                                                                                                              a5, a10,
                                                                                                              a15))

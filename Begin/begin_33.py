# Задание №32
# Дано значение температуры T в градусах Цельсия. Определить зна-
# чение этой же температуры в градусах Фаренгейта. Температура по Цель-
# сию TC и температура по Фаренгейту TF связаны следующим соотноше-
# нием:
# TC = (TF − 32)·5/9.

TC = float(input())
TF = ((TC * 9 / 5) + 32)
print('Температура {} градусов цельсия будет равна {} градусов по фаренгейту'.format(round(TC, 2), round(TF, 2)))

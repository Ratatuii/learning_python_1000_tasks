# Задание №30
# Дано значение температуры T в градусах Фаренгейта. Определить
# значение этой же температуры в градусах Цельсия. Температура по Цель-
# сию TC и температура по Фаренгейту TF связаны следующим соотноше-
# нием:
# TC = (TF − 32)*5/9.

TF = float(input())
TC = ((TF - 32) * 5 / 9)
print('Температура {} градусов по фаренгейту будет равна {} градусов цельсия'.format(round(TF, 2), round(TC, 2)))

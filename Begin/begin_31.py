# Задание №30
# Дано значение угла α в радианах (0 < α < 2·π). Определить значение
# этого же угла в градусах, учитывая, что 180 ◦ = π радианов. В качестве
# значения π использовать 3.14.
pi = 3.14
a_rad = float(input())
a_deg = (pi * 180) / a_rad
# print('Значения угла α в градусах = {} в радианах = {}'.format(a_deg, round(a_rad, 6)))
print('Значение угла α в радианах = {}, в градусах = {}'.format(a_rad, round(a_deg, 5)))

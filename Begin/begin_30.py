# Задание №29
# Дано значение угла α в градусах (0 < α < 360). Определить значение
# этого же угла в радианах, учитывая, что 180 ◦ = π радианов. В качестве
# значения π использовать 3.14.
pi = 3.14
a_deg = int(input())
a_rad = a_deg * (pi / 180)
print('Значения угла α в градусах = {} в радианах = {}'.format(a_deg, round(a_rad, 6)))

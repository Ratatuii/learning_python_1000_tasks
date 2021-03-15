# Задание №33
# Известно, что X кг конфет стоит A рублей. Определить, сколько
# стоит 1 кг и Y кг этих же конфет.

x = int(input())
a = int(input())
y = int(input())
cost_1_kg = a / x
cost_y_kg = cost_1_kg * y
print('Стоимость 1 кг конфет {} рублей, a стоимость {} кг конфет стоит {} рублей'.format(round(cost_1_kg, 4), y,
                                                                                         round(cost_y_kg, 4)))

pi = 3.14

tmp = True

while tmp == True:
    r1 = int(input('Введите радиус R1 первого круга: '))
    r2 = int(input('Введите радиус R2 второго круга: '))
    s1 = pi * r1 ** 2
    s2 = pi * r2 ** 2
    s3 = s1 - s2
    if r1 > r2:
        print('Площадь круга R1 - {} = {}'.format(r1, s1))
        print('Площадь круга R2 - {} = {}'.format(r2, s2))
        print('Площадь круга R3 - {} = {}'.format(r2, s3))
        tmp == False
        break
    else:
        print('Радиус R2 должен быть больше чем радиус R1. Попробуйте еще раз.')

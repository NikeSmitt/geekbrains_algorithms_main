# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing

# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

a, b, c = map(float, input('Введите длину трех отрезков через пробел -> ').split())

long = a
if long < b:
    short_1 = a
    long = b
else:
    short_1 = b

if long < c:
    short_2 = b
    long = c
else:
    short_2 = c

if long - short_1 - short_1 < 0:
    if long == short_1 and long == short_2:
        print('Треугольник равносторонний')
    elif short_1 == short_2:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')

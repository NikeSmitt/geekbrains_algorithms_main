# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = map(float, input('Введите три разных числа через пробел -> ').split())

if a > b:
    if a < c:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)
else:
    if b > c:
        if c > a:
            print(c)
        else:
            print(a)
    else:
        print(b)


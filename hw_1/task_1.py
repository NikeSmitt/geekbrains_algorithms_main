# https://drive.google.com/file/d/1HGPRvqvPN5kyVOUwwkM6X3Ua8kwnFTan/view?usp=sharing

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите число от 100 до 999: '))

original = x
summ = 0
mult = 1

last = x % 10

summ += last
mult *= last

x //= 10

last = x % 10

summ += last
mult *= last

last = x // 10

summ += last
mult *= last

print(f'Число {original}. Сумма цифр: {summ}, Произведение цифр: {mult}')
